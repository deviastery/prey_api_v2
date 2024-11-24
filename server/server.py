from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

con = sqlite3.connect("prey.db", check_same_thread=False)
cursor = con.cursor()
print("success")

@app.route("/api/v1/", methods=["GET"])
def return_home():
    return jsonify({
        "hostiles": "http:/localhost:3001/api/hostiles/",
        "abilities": "http:/localhost:3001/api/abilities/",
        "chipsets": "http:/localhost:3001/api/chipsets/",
        "locations": "http:/localhost:3001/api/locations/",
        "weapons": "http:/localhost:3001/api/weapons/"
    })

@app.route("/api/v1/hostiles", methods=["GET"])
def get_hostiles():
  try:
    cursor.execute("SELECT id, name, image_url, research_count, scientific_name FROM hostiles") # Запрос к базе данных
    hostiles = cursor.fetchall()
    # Преобразуем результат в более удобный формат JSON
    hostiles_list = [{'id': row[0], 'name': row[1], 'image_url': row[2], 'research_count': row[3], 'scientific_name': row[4]} for row in hostiles]
    return jsonify(hostiles_list)
  except sqlite3.Error as e:
    return jsonify({"error": str(e)}), 500 # Возвращаем ошибку 500 (Internal Server Error)
  finally:
    # Не закрываем соединение здесь, чтобы оно оставалось открытым для всех запросов
    pass

@app.route("/api/v1/hostiles/<int:hostile_id>", methods=["GET"])
def get_hostile(hostile_id):
  try:
      cursor.execute("SELECT * FROM hostiles WHERE id = ?", (hostile_id,))  # Используем параметризованный запрос
      hostile = cursor.fetchone()  # fetchone() для получения одной строки

      if hostile is None:
          return jsonify({"error": "Hostile not found"}), 404  # Возвращаем 404, если запись не найдена

      # Преобразуем результат в JSON.  Более эффективный метод, не требующий знания количества столбцов:
      hostile_dict = dict(zip([col[0] for col in cursor.description], hostile))
      return jsonify(hostile_dict)

  except sqlite3.Error as e:
      return jsonify({"error": str(e)}), 500 # Возвращаем ошибку 500 (Internal Server Error)
  finally:
    # Не закрываем соединение здесь, чтобы оно оставалось открытым для всех запросов
    pass

@app.route("/api/v1/abilities", methods=["GET"])
def get_abilities():
  try:
    cursor.execute("SELECT id, name, type FROM abilities") # Запрос к базе данных
    abilities = cursor.fetchall()
    # Преобразуем результат в более удобный формат JSON
    abilities_list = [{'id': row[0], 'name': row[1], 'type': row[2]} for row in abilities]
    return jsonify(abilities_list)
  except sqlite3.Error as e:
    return jsonify({"error": str(e)}), 500 # Возвращаем ошибку 500 (Internal Server Error)
  finally:
    # Не закрываем соединение здесь, чтобы оно оставалось открытым для всех запросов
    pass

@app.route("/api/v1/abilities/<int:ability_id>", methods=["GET"])
def get_ability(ability_id):
  try:
      cursor.execute("SELECT * FROM abilities WHERE id = ?", (ability_id,))  # Используем параметризованный запрос
      ability = cursor.fetchone()  # fetchone() для получения одной строки

      if ability is None:
          return jsonify({"error": "Hostile not found"}), 404  # Возвращаем 404, если запись не найдена

      # Преобразуем результат в JSON.  Более эффективный метод, не требующий знания количества столбцов:
      ability_dict = dict(zip([col[0] for col in cursor.description], ability))
      return jsonify(ability_dict)

  except sqlite3.Error as e:
      return jsonify({"error": str(e)}), 500 # Возвращаем ошибку 500 (Internal Server Error)
  finally:
    # Не закрываем соединение здесь, чтобы оно оставалось открытым для всех запросов
    pass

@app.route("/api/v1/chipsets", methods=["GET"])
def get_chipsets():
  try:
    cursor.execute("SELECT id, name, type, description FROM chipsets") # Запрос к базе данных
    chipsets = cursor.fetchall()
    # Преобразуем результат в более удобный формат JSON
    chipsets_list = [{'id': row[0], 'name': row[1], 'type': row[2], 'description': row[3]} for row in chipsets]
    return jsonify(chipsets_list)
  except sqlite3.Error as e:
    return jsonify({"error": str(e)}), 500 # Возвращаем ошибку 500 (Internal Server Error)
  finally:
    # Не закрываем соединение здесь, чтобы оно оставалось открытым для всех запросов
    pass

@app.route("/api/v1/chipsets/<int:chipset_id>", methods=["GET"])
def get_chipset(chipset_id):
  try:
      cursor.execute("SELECT * FROM chipsets WHERE id = ?", (chipset_id,))  # Используем параметризованный запрос
      chipset = cursor.fetchone()  # fetchone() для получения одной строки

      if chipset is None:
          return jsonify({"error": "Hostile not found"}), 404  # Возвращаем 404, если запись не найдена

      # Преобразуем результат в JSON.  Более эффективный метод, не требующий знания количества столбцов:
      ability_dict = dict(zip([col[0] for col in cursor.description], chipset))
      return jsonify(ability_dict)

  except sqlite3.Error as e:
      return jsonify({"error": str(e)}), 500 # Возвращаем ошибку 500 (Internal Server Error)
  finally:
    # Не закрываем соединение здесь, чтобы оно оставалось открытым для всех запросов
    pass

@app.route("/api/v1/locations", methods=["GET"])
def get_locations():
  try:
    cursor.execute("SELECT id, name, med_bay, crew_assigned, airlock FROM locations") # Запрос к базе данных
    locations = cursor.fetchall()
    # Преобразуем результат в более удобный формат JSON
    locations_list = [{'id': row[0], 'name': row[1], 'med_bay': row[2], 'crew_assigned': row[3], 'airlock': row[4]} for row in locations]
    return jsonify(locations_list)
  except sqlite3.Error as e:
    return jsonify({"error": str(e)}), 500 # Возвращаем ошибку 500 (Internal Server Error)
  finally:
    # Не закрываем соединение здесь, чтобы оно оставалось открытым для всех запросов
    pass

@app.route("/api/v1/locations/<int:location_id>", methods=["GET"])
def get_location(location_id):
  try:
      cursor.execute("SELECT * FROM locations WHERE id = ?", (location_id,))  # Используем параметризованный запрос
      location = cursor.fetchone()  # fetchone() для получения одной строки

      if location is None:
          return jsonify({"error": "Hostile not found"}), 404  # Возвращаем 404, если запись не найдена

      # Преобразуем результат в JSON.  Более эффективный метод, не требующий знания количества столбцов:
      location_dict = dict(zip([col[0] for col in cursor.description], location))
      return jsonify(location_dict)

  except sqlite3.Error as e:
      return jsonify({"error": str(e)}), 500 # Возвращаем ошибку 500 (Internal Server Error)
  finally:
    # Не закрываем соединение здесь, чтобы оно оставалось открытым для всех запросов
    pass

@app.route("/api/v1/weapons", methods=["GET"])
def get_weapons():
  try:
    cursor.execute("SELECT id, name, primary_fire, rate_of_fire, secondary_fire, firing_range FROM weapons") # Запрос к базе данных
    weapons = cursor.fetchall()
    # Преобразуем результат в более удобный формат JSON
    weapons_list = [{'id': row[0], 'name': row[1], 'primary_fire': row[2], 'rate_of_fire': row[3], 'secondary_fire': row[4], 'firing_range': row[5]} for row in weapons]
    return jsonify(weapons_list)
  except sqlite3.Error as e:
    return jsonify({"error": str(e)}), 500 # Возвращаем ошибку 500 (Internal Server Error)
  finally:
    # Не закрываем соединение здесь, чтобы оно оставалось открытым для всех запросов
    pass

@app.route("/api/v1/weapons/<int:weapon_id>", methods=["GET"])
def get_weapon(weapon_id):
  try:
      cursor.execute("SELECT * FROM weapons WHERE id = ?", (weapon_id,))  # Используем параметризованный запрос
      weapon = cursor.fetchone()  # fetchone() для получения одной строки

      if weapon is None:
          return jsonify({"error": "Hostile not found"}), 404  # Возвращаем 404, если запись не найдена

      # Преобразуем результат в JSON.  Более эффективный метод, не требующий знания количества столбцов:
      weapon_dict = dict(zip([col[0] for col in cursor.description], weapon))
      return jsonify(weapon_dict)

  except sqlite3.Error as e:
      return jsonify({"error": str(e)}), 500 # Возвращаем ошибку 500 (Internal Server Error)
  finally:
    # Не закрываем соединение здесь, чтобы оно оставалось открытым для всех запросов
    pass

if __name__ == "__main__":
    app.run(debug=False)