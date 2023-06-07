import sqlite3

class PreparationIntegratedDatabase:
    def prepare_integrated_db(self):
        connection = sqlite3.connect("integratedDB.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS pokemon(pokemon_id PRIMARY KEY, pokemon_internal_name, pokemon_name, pokemon_type_1, pokemon_type_2, pokemon_base_hp, pokemon_base_atk, pokemon_base_def, pokemon_base_spe, pokemon_base_spa, pokemon_base_spd, pokemon_gender_ratio, pokemon_growth_rate, pokemon_base_exp, pokemon_ev, pokemon_ev_gain, pokemon_catch_rate, pokemon_happiness, pokemon_hatch_steps, pokemon_height, pokemon_weight, pokemon_color, pokemon_shape, pokemon_habitat, pokemon_category, pokemon_pokedex, pokemon_generation)")
        cursor.execute("CREATE TABLE IF NOT EXISTS pokemon_forms(form_id PRIMARY KEY, form_original_pokemon, form_name, form_type_1, form_type_2, form_base_hp, form_base_atk, form_base_def, form_base_spe, form_base_spa, form_base_spd, form_gender_ratio, form_base_exp, form_ev, form_ev_gain, form_catch_rate, form_happiness, form_hatch_steps, form_height, form_weight, form_color, form_habitat, form_category, form_pokedex, form_generation)")
        cursor.execute("CREATE TABLE IF NOT EXISTS types(type_id PRIMARY KEY,type_internal_name, type_icon_position, type_name)")
        cursor.execute("CREATE TABLE IF NOT EXISTS moves(move_id PRIMARY KEY, move_internal_name, move_name, move_category, move_power, move_accuracy, move_total_pp, move_target, move_function_code, move_description)")
        cursor.execute("CREATE TABLE IF NOT EXISTS abilities(ability_id PRIMARY KEY, ability_internal_name, ability_name, ability_description)")
        cursor.execute("CREATE TABLE IF NOT EXISTS items(item_id PRIMARY KEY, item_internal_name, item_name, item_name_plural, item_pocket, item_price, item_field_use, item_description)")
        cursor.execute("CREATE TABLE IF NOT EXISTS trainers(trainer_id PRIMARY KEY, trainer_name)")
        cursor.execute("CREATE TABLE IF NOT EXISTS trainer_pokemon(tp_id PRIMARY KEY, tp_trainer, tp_pokemon, tp_move_1, tp_move_2, tp_move_3, tp_move_4)")
        cursor.execute("CREATE TABLE IF NOT EXISTS trainer_items(ti_id PRIMARY KEY, ti_trainer, ti_item)")
        cursor.execute("CREATE TABLE IF NOT EXISTS type_effectiveness(te_id PRIMARY KEY, te_attacking_type, te_defending_type, te_effectiveness)")
        cursor.execute("CREATE TABLE IF NOT EXISTS locations(location_id PRIMARY KEY, location_name)")
        cursor.execute("CREATE TABLE IF NOT EXISTS location_items(li_id PRIMARY KEY, li_location, li_item, li_method)")
        cursor.execute("CREATE TABLE IF NOT EXISTS location_trainers(lt_id PRIMARY KEY, lt_location, lt_trainer_id)")
        cursor.execute("CREATE TABLE IF NOT EXISTS location_encounters(le_id PRIMARY KEY, le_location, le_pokemon, le_season, le_percentage, le_min_level, le_max_level)")
        cursor.execute("CREATE TABLE IF NOT EXISTS move_flags(mf_id PRIMARY KEY, mf_move, mf_flag)")
        cursor.execute("CREATE TABLE IF NOT EXISTS item_flags(if_id PRIMARY KEY, if_item, if_flag)")
        cursor.execute("CREATE TABLE IF NOT EXISTS pokemon_learnset(pl_id PRIMARY KEY, pl_pokemon, pl_move, pl_level)")
        cursor.execute("CREATE TABLE IF NOT EXISTS pokemon_tutor_moves(ptl_id PRIMARY KEY, ptl_pokemon, ptl_move)")
        cursor.execute("CREATE TABLE IF NOT EXISTS pokemon_egg_moves(pem_id PRIMARY KEY, pem_pokemon, pem_move)")
        cursor.execute("CREATE TABLE IF NOT EXISTS pokemon_ability(pa_id PRIMARY KEY, pa_pokemon, pa_pokemon_form, pa_ability, pa_hidden)")
        cursor.execute("CREATE TABLE IF NOT EXISTS egg_groups(eg_id PRIMARY KEY, eg_name)")
        cursor.execute("CREATE TABLE IF NOT EXISTS pokemon_egg_groups(peg_id PRIMARY KEY, peg_pokemon, peg_egg_group)")
        cursor.execute("CREATE TABLE IF NOT EXISTS pokemon_evolution(pe_id PRIMARY KEY, pe_from_id, pe_to_id, pe_method, pe_additional_requirement)")

        connection.close()

if __name__ == "__main__":
    pid = PreparationIntegratedDatabase()
    pid.prepare_integrated_db()