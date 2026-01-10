from flask import Flask, render_template, url_for,request,redirect

print("### PART 4 APP.PY IS RUNNING ###")

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('index.html')


# ---------------- ABOUT ----------------
@app.route('/about/')
def about():
    return render_template('about.html')


# ---------------- USER PROFILE ----------------
@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', username=username)


# ---------------- POST ----------------
@app.route('/post/<int:post_id>')
def show_post(post_id):
    posts = {
        1: {'title': 'Getting Started with Flask', 'content': 'Flask is a micro-framework...'},
        2: {'title': 'Understanding Routes', 'content': 'Routes map URLs to functions...'},
        3: {'title': 'Working with Templates', 'content': 'Jinja2 makes HTML dynamic...'},
    }
    post = posts.get(post_id)
    return render_template('post.html', post_id=post_id, post=post)


# ---------------- USER POST ----------------
@app.route('/user/<username>/post/<int:post_id>')
def user_post(username, post_id):
    return render_template('user_post.html', username=username, post_id=post_id)


# ---------------- LINKS (Navigation Menu) ----------------
@app.route('/links')
def show_links():
    links = {
        'Home': url_for('home'),
        'About': url_for('about'),
        'User Alice': url_for('user_profile', username='Alice'),
        'User Bob': url_for('user_profile', username='Bob'),
        'Post 1': url_for('show_post', post_id=1),
        'Post 2': url_for('show_post', post_id=2),
        'Search Laptop': url_for('search_result', query='laptop'),

        # ✅ Exercise 4.2 – Category + Product Navigation
        'Electronics - Mobile': url_for('category_product', category_name='electronics', product_id=1),
        'Electronics - Laptop': url_for('category_product', category_name='electronics', product_id=2),
        'Clothing - T-Shirt': url_for('category_product', category_name='clothing', product_id=1),
        'Clothing - Jeans': url_for('category_product', category_name='clothing', product_id=2),
    }

    return render_template('links.html', links=links)


# =================================================
# EXERCISE 4.1 – PRODUCT PAGE
# =================================================
@app.route('/product/')
def product_default():
    product = {'name': 'Laptop', 'price': 55000}
    product_id = 1
    return render_template('product.html', product=product, product_id=product_id)


@app.route('/product/<int:product_id>')
def product_page(product_id):
    products = {
        1: {'name': 'Laptop', 'price': 55000},
        2: {'name': 'Mobile', 'price': 20000},
        3: {'name': 'Headphones', 'price': 2500},
    }

    product = products.get(product_id)
    return render_template('product.html', product=product, product_id=product_id)


# ---------------- CATEGORY + PRODUCT ----------------
@app.route('/category/<category_name>/product/<int:product_id>')
def category_product(category_name, product_id):

    products = {
        "electronics": {
            1: {"name": "Mobile Phone", "price": 15000},
            2: {"name": "Laptop", "price": 55000}
        },
        "clothing": {
            1: {"name": "T-Shirt", "price": 800},
            2: {"name": "Jeans", "price": 2000}
        }
    }

    product = products.get(category_name, {}).get(product_id)

    return render_template(
        'index.html',
        show_category_product=True,    # ✅ ONLY HERE
        product=product,
        product_id=product_id,
        category_name=category_name
    )


# =================================================
# ✅ EXERCISE 4.3 – SEARCH ROUTE
# =================================================

# Handle search form (GET request)
@app.route('/search')
def search_form():
    query = request.args.get('q')

    if not query:
        return redirect(url_for('home'))

    return redirect(url_for('search_result', query=query))


# Display search result
@app.route('/search/<query>')
def search_result(query):
    return render_template('search.html', query=query)


# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# URL PARAMETER TYPES:
# =============================================================================
#
# <variable>         - String (default), accepts any text without slashes
# <int:variable>     - Integer, accepts only positive integers
# <float:variable>   - Float, accepts floating point numbers
# <path:variable>    - String, but also accepts slashes
# <uuid:variable>    - UUID strings
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 4.1: Create a product page
#   - Add route /product/<int:product_id>
#   - Create a products dictionary with id, name, price
#   - Display product details or "Not Found" message
#
# Exercise 4.2: Category and product route
#   - Add route /category/<category_name>/product/<int:product_id>
#   - Display both the category and product information
#
# Exercise 4.3: Search route
#   - Add route /search/<query>
#   - Display "Search results for: [query]"
#   - Bonus: Add a simple search form that redirects to this route
#
# =============================================================================