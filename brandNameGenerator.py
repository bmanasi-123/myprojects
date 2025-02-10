# # Brand Name Generator
#
# def generator(city: str, pet: str) -> str:
#     return city.capitalize() + ' ' + pet.capitalize()
#
# def userInput():
#
#     city = input("What's your Birth city name ? ")
#     pet = input("What's your Pet name ? ")
#     return city, pet
#
# if __name__ == "__main__":
#
#     flag = True
#     print("Welcome to Brand-Name-Generator !!! ")
#     while flag:
#
#         city, pet = userInput()
#         print("Your Brand name could be :", generator(city, pet))
#         response = input('''
# To continue type : Continue
# To exit type : Exit
# ''')
#         if response.lower() == 'exit':
#             flag = False
#

# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
# # Brand Name Generator Function
# def generator(city: str, pet: str) -> str:
#     return city.capitalize() + ' ' + pet.capitalize()
#
# @app.route('/', methods=['GET', 'POST'])
# def home():
#     brand_name = ''
#     if request.method == 'POST':
#         city = request.form['city']
#         pet = request.form['pet']
#         brand_name = generator(city, pet)
#     return render_template('index.html', brand_name=brand_name)
#
# if __name__ == "__main__":
#     app.run(debug=True, port=9001)

from flask import Flask, render_template, request

app = Flask(__name__)

# Predefined options for each category
categories = {
    "city": ["New York", "Los Angeles", "Chicago", "Miami", "San Francisco"],
    "pet": ["Bella", "Max", "Charlie", "Luna", "Rocky"],
    "partner": ["Alex", "Jordan", "Taylor", "Morgan", "Casey"],
    "sports": ["Soccer", "Basketball", "Tennis", "Baseball", "Swimming"],
    "series": ["Stranger Things", "Breaking Bad", "The Crown", "Friends", "The Office"]
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/choose_option', methods=['POST'])
def choose_option():
    option = request.form.get('option')

    if option == 'makeOwn':
        return render_template('make_own.html')
    elif option == 'suggested':
        return render_template('suggested.html')
    return render_template('index.html')


@app.route('/make_own', methods=['POST'])
def make_own():
    city = request.form.get('city')
    pet = request.form.get('pet')
    partner = request.form.get('partner')
    sports = request.form.get('sports')
    series = request.form.get('series')

    # Collect valid inputs
    inputs = [city, pet, partner, sports, series]
    selected_inputs = [i for i in inputs if i]

    if len(selected_inputs) < 2:
        brand_name = "Please fill in at least two categories."
    else:
        # Generate a brand name using any two inputs
        brand_name = selected_inputs[0].capitalize() + " " + selected_inputs[1].capitalize()

    return render_template('result.html', brand_name=brand_name)


@app.route('/suggested', methods=['POST'])
def suggested():
    category1 = request.form.get('category1')
    category2 = request.form.get('category2')

    # Ensure categories are not the same
    if category1 == category2:
        return render_template('suggested.html', error="Please select two different categories.")

    # Randomly choose from each category
    import random
    option1 = random.choice(categories[category1])
    option2 = random.choice(categories[category2])

    brand_name = option1.capitalize() + " " + option2.capitalize()

    return render_template('result.html', brand_name=brand_name)


if __name__ == '__main__':
    app.run(debug=True, port=9001)
