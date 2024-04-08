from flask import Flask, request, jsonify # type: ignore
import sqlite3

app = Flask(__name__)

def create_table():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       description TEXT,
                       price REAL)''')
    conn.commit()
    conn.close()

create_table()

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM products WHERE id = ?''', (id,))
    product = cursor.fetchone()
    conn.close()
    if product:
        return jsonify({'product': product}), 200
    else:
        return jsonify({'message': 'Product not found'}), 404


@app.route('/products', methods=['GET'])
def get_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM products''')
    products = cursor.fetchall()
    conn.close()
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    name = data['name']
    description = data['description']
    price = data['price']
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO products (name, description, price) VALUES (?, ?, ?)''',
                   (name, description, price))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product added successfully'}),201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM products WHERE id = ?''', (id,))
    produto = cursor.fetchone()
    conn.close()

    if produto is None:
        return jsonify({'error': 'Product not found'}), 404

    data = request.json
    name = data['name']
    description = data['description']
    price = data['price']

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE products SET name=?, description=?, price=? WHERE id=?''',
                   (name, description, price, id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product updated successfully'})

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM products WHERE id = ?''', (id,))
    produto = cursor.fetchone()
    
    if produto is None:
        conn.close()
        return jsonify({'error': 'Product not found'}), 404

    cursor.execute('''DELETE FROM products WHERE id = ?''', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Product deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
