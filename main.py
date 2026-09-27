from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    level_current=0
    level_target=0
    need_xp=0
    if request.method == 'POST':
        level_current = request.form.get('level_current', type=int)
        level_target = request.form.get('level_target', type=int)
        if level_current>=32:
            level_current_1=level_current*level_current*4.5
            level_current_2=level_current*162.5
            level_current=level_current_1-level_current_2+2200
        if level_target>=32:
            level_target_1=level_target*level_target*4.5
            level_target_2=level_target*162.5
            level_target=level_target_1-level_target_2+2200
        if level_current<=31 and level_current>=17:
            level_current_1=level_current*level_current*2.5
            level_current_2=level_current*40.5
            level_current=level_current_1-level_current_2+360
        if level_target<=31 and level_target>=17:
            level_target_1=level_target*level_target*2.5
            level_target_2=level_target*40.5
            level_target=level_target_1-level_target_2+360
        if level_current<=16:
            level_current_1=level_current*level_current
            level_current_2=6*level_current
            level_current=level_current_1+level_current_2
        if level_target<=16:
            level_target_1=level_target*level_target
            level_target_2=6*level_target
            level_target=level_target_1+level_target_2
        need_xp=level_target-level_current
    return render_template('index.html', level_current=level_current, level_target=level_target , need_xp=need_xp)

app.run(debug=True)