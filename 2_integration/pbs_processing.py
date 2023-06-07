import sqlite3


class PbsProcessing:
    def process_pokemon(self):
        file = open("../0_datasets/pokemon.txt", "r")
        lines = file.readlines()

    def process_types(self):
        file = open("../0_datasets/types.txt", "r")
        lines = file.readlines()

        connection = sqlite3.connect("integratedDB.db")
        cursor = connection.cursor()
        for line in lines:
            split_line = line.strip("\n[]").split(" = ")


            if split_line[0].find("#") == -1 :
                if len(split_line) > 1:
                    if split_line[0] == "Name":
                        last_id = self.get_last_id(cursor, "types")
                        cursor.execute("UPDATE types SET type_name = ? WHERE type_id = ?", (split_line[1], last_id))
                    elif split_line[0] == "IconPosition":
                        last_id = self.get_last_id(cursor, "types")
                        cursor.execute("UPDATE types SET type_icon_position = ? WHERE type_id = ?", (split_line[1], last_id))
                    elif split_line[0] == "Weaknesses":
                        split_types = split_line[1].split(",")
                        last_te_id = self.get_last_id(cursor, "type_effectiveness")
                        next_id = last_te_id + 1
                        last_type_id = self.get_last_id(cursor, "types")
                        defending_type = cursor.execute("SELECT type_internal_name FROM types WHERE type_id = ?", (last_type_id))
                        for type in split_types:
                            cursor.execute("INSERT INTO type_effectiveness VALUES (?,?,?,?)", (next_id, type, defending_type, "WEAK"))
                            next_id += 1
                    elif split_line[0] == "Resistances":
                        split_types = split_line[1].split(",")
                        last_te_id = self.get_last_id(cursor, "type_effectiveness")
                        next_id = last_te_id + 1
                        last_type_id = self.get_last_id(cursor, "types")
                        defending_type = cursor.execute("SELECT type_internal_name FROM types WHERE type_id = ?", (last_type_id))
                        for type in split_types:

                            cursor.execute("INSERT INTO type_effectiveness VALUES (?,?,?,?)", (next_id, type, defending_type, "RESISTANT"))
                            next_id += 1
                    elif split_line[0] == "Immunities":
                        split_types = split_line[1].split(",")
                        last_te_id = self.get_last_id(cursor, "type_effectiveness")
                        next_id = last_te_id + 1
                        last_type_id = self.get_last_id(cursor, "types")
                        defending_type = cursor.execute("SELECT type_internal_name FROM types WHERE type_id = ?", (last_type_id))
                        for type in split_types:

                            cursor.execute("INSERT INTO type_effectiveness VALUES (?,?,?,?)", (next_id, type, defending_type, "IMMUNE"))
                            next_id += 1


                    else:
                        pass

                else:
                    last_id = self.get_last_id(cursor, "types")
                    new_id = last_id + 1
                    data = [(new_id, split_line[0])]
                    cursor.executemany("INSERT INTO types (type_id, type_internal_name) VALUES (?,?)", data)

        connection.close()

    def get_last_id(self, cursor, table):
        if table == "pokemon":
            res = cursor.execute("SELECT pokemon_id FROM pokemon")
            ids = res.fetchall()
            if len(ids) == 0:
                return 0
            else:
                return ids[-1]
        elif table == "pokemon_forms":
            res = cursor.execute("SELECT form_id FROM pokemon_forms")
            ids = res.fetchall()
            if len(ids) == 0:
                return 0
            else:
                return ids[-1]
        elif table == "types":
            res = cursor.execute("SELECT type_id FROM types")
            ids = res.fetchall()
            if len(ids) == 0:
                return 0
            else:
                return ids[-1]#
        elif table == "moves":
            res = cursor.execute("SELECT move_id FROM moves")
            ids = res.fetchall()
            if len(ids) == 0:
                return 0
            else:
                return ids[-1]
        elif table == "abilities":
            res = cursor.execute("SELECT ability_id FROM abilities")
            ids = res.fetchall()
            if len(ids) == 0:
                return 0
            else:
                return ids[-1]
        elif table == "items":
            res = cursor.execute("SELECT item_id FROM items")
            ids = res.fetchall()
            if len(ids) == 0:
                return 0
            else:
                return ids[-1]
        elif table == "trainers":
            res = cursor.execute("SELECT trainer_id FROM trainers")
            ids = res.fetchall()
            if len(ids) == 0:
                return 0
            else:
                return ids[-1]
        elif table == "trainer_pokemon":
            res = cursor.execute("SELECT tp_id FROM trainer_pokemon")
            ids = res.fetchall()
            if len(ids) == 0:
                return 0
            else:
                return ids[-1]
        elif table == "trainer_items":
            res = cursor.execute("SELECT ti_id FROM trainer_items")
            ids = res.fetchall()
            if len(ids) == 0:
                return 0
            else:
                return ids[-1]
        elif table == "type_effectiveness":
            res = cursor.execute("SELECT te_id FROM type_effectiveness")
            ids = res.fetchall()
            if len(ids) == 0:
                return 0
            else:
                return ids[-1]

if __name__ == "__main__":
    pbs_p = PbsProcessing()
    pbs_p.process_types()

