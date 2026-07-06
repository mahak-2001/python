# python={"mahak","jiya","twinkle","jaanvi"}
# sql={"preeti","deepika","mahak","rinku"}
# print(python.intersection(sql))
person={
    "person_1":{
        "name":"mahak",
        "course":"BCA"
    },
    "person_2":{
        "name":"ram",
        "course":"BBA"
    }
}
# print(person["person_1"]["name"])
# print(person["person_2"]["email","email not found"])
print(person["person_2"].get("email","not found"))
