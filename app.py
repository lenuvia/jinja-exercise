from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)

@app.route('/')
def story_questions():
  prompts = story.prompts
  return render_template('form.html', prompts=prompts)

@app.route('/story')
def story_page():
  text = story.generate(request.args)
  return render_template('story.html', text=text)