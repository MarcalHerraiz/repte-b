x = 0

def on_button_pressed_a():
    music.play(music.string_playable("G F G A - F E D ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play(music.string_playable("C D E F G A B C5 ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    global x
    led.plot_bar_graph(input.acceleration(Dimension.X), 1023)
    x = input.acceleration(Dimension.X)
    if x > 300:
        music.change_tempo_by(20)
basic.forever(on_forever)
