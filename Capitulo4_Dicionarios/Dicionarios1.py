usuarios = {}
usuarios = {
    "Chaves": ["Chaves Silva", "17/06/1975", "Recep_01"],
    "Quico": ["Enrico Flores", "03/06/1976", "Raiox_02"],
    "Quico": ["Enrico Flores", "03/06/1976", "Raiox_03"],
}
usuarios["Florinda"] = ["Florinda Flores", "26/11/2017", "Recep_01"]
# Se tentar adicionar a mesma linha, o compilador só considerará a última
usuarios["Florinda"] = ["Florinda Flores", "26/11/2016", "Recep_01"]

print(usuarios)
print("##############========#########")
print("Dados: ", usuarios.get("Chaves"))
