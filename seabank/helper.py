JF_PRODUCT = {
    101 : "SPL",
    102 : "SPL",
    103 : "BCL",
    104 : "BCL",
    105 : "SCL",
}

DB_PRODUCT = {
    106 : "KPL",
    107 : "EML"
}

BV_PRODUCT = {
    108 : "Channeling",
}


all_product = JF_PRODUCT | DB_PRODUCT | BV_PRODUCT
list_product = [(k,v) for k, v in all_product.items()]

print(list_product)