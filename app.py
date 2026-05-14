from flask import Flask, render_template
from data import (
    VOCABULARY, PHRASAL_VERBS, VERBS_PREPOSITIONS, COLLOCATIONS,
    CONNECTORS, IDIOMS, CONFUSING_EXPRESSIONS, GRAMMAR_EXERCISES,
    USE_OF_ENGLISH, CAMBRIDGE_TEST_1,
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/vocabulary")
def vocabulary():
    return render_template("vocabulary.html", words=VOCABULARY)


@app.route("/phrasal-verbs")
def phrasal_verbs():
    return render_template("phrasal_verbs.html", items=PHRASAL_VERBS)


@app.route("/verbs-prepositions")
def verbs_prepositions():
    return render_template("verbs_prepositions.html", items=VERBS_PREPOSITIONS)


@app.route("/collocations")
def collocations():
    return render_template("collocations.html", items=COLLOCATIONS)


@app.route("/connectors")
def connectors():
    return render_template("connectors.html", items=CONNECTORS)


@app.route("/idioms")
def idioms():
    return render_template("idioms.html", items=IDIOMS)


@app.route("/confusing-expressions")
def confusing_expressions():
    return render_template("confusing_expressions.html", items=CONFUSING_EXPRESSIONS)


@app.route("/grammar")
def grammar():
    return render_template("grammar.html", exercises=GRAMMAR_EXERCISES)


@app.route("/use-of-english")
def use_of_english():
    return render_template("use_of_english.html", exercises=USE_OF_ENGLISH, cambridge=CAMBRIDGE_TEST_1)


if __name__ == "__main__":
    app.run(debug=True)
