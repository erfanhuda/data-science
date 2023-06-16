-- QUERY FOR LOOKING AT ODR BY SYSTEM

SELECT
    pd_segment,
    tenor,
    qoq_date,
    pt_date,
    avg(odr_loan)
FROM
    ecl.rep_fin_ecl_pd_odr_qoq_ss_m
where
    qoq_date between '2022-10-31' and '2023-03-31'
group by
    pd_segment,
    tenor,
    qoq_date,
    pt_date;

-- QUERY FOR CLOSING AND PRECLOSING RAW DATA

select
    pt_date,
    tenor,
    day_past_due,
    max_dpd,
    ecl_bucket,
    max_ecl as max_ecl_cif_level,
    collectability,
    col,
    product_code,
    loan_disbursement_date,
    loan_maturity_date,
    -- substring (a.loan_disbursement_date,1,7) as	disburse_month,
    count(1) as loan_no,
    sum(loan_disb) as loan_disb,
    sum(cur_balance) as cur_balance,
    sum(total_int_accrued) as total_int_accrued,
    sum(total_int_accrued_adj) as total_int_accrued_adj,
    sum(fac_amount) as fac_amount,
    a.int_real_rate,
    a.tenor_in_month
from (
        select *
        from
            dm.rep_fin_reg_db_master_kredit_ss_d
        where
            pt_date = '2023-05-30'
    ) as a
    join (
        select
            b.client_no,
            max (cast (b.ecl_bucket as numeric)) as max_ecl,
            max (
                cast (b.day_past_due as numeric)
            ) as max_dpd
        from
            dm.rep_fin_reg_db_master_kredit_ss_d as b
        where
            pt_date = '2023-05-30'
        group by
            client_no
    ) as c on (a.client_no = c.client_no)
group by
    pt_date,
    tenor,
    ecl_bucket,
    max_ecl,
    col,
    product_code,
    -- substring (a.loan_disbursement_date,1,7)
    day_past_due,
    collectability,
    loan_disbursement_date,
    loan_maturity_date,
    max_dpd,
    a.int_real_rate,
    a.tenor_in_month;