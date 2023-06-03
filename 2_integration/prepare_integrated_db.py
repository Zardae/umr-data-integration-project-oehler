import sqlite3

def prepare_integrated_db():
    connection = sqlite3.connect("integratedDB.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS types(type_id PRIMARY KEY, type_name)")
    cursor.execute("CREATE TABLE IF NOT EXISTS type_effectiveness(te_id PRIMARY KEY, attacking_type, defending_type, effectiveness)")
    cursor.execute("CREATE TABLE IF NOT EXISTS moves(move_id PRIMARY KEY, move_name, move_type, category, power, accuracy, total_pp, target, function_code, move_description)")
    cursor.execute("CREATE TABLE IF NOT EXISTS move_flags(mf_id PRIMARY KEY, move, flag)")
    cursor.execute("CREATE TABLE IF NOT EXISTS abilities(ability_id PRIMARY KEY, ability_name, ability_description)")

    res = cursor.execute("SELECT name FROM sqlite_master")
    print(res.fetchall())

    connection.close()




if __name__ == "__main__":
    prepare_integrated_db()