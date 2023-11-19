let x = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.play(music.stringPlayable("G F G A - F E D ", 120), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    music.play(music.stringPlayable("C D E F G A B C5 ", 120), music.PlaybackMode.UntilDone)
})
basic.forever(function on_forever() {
    
    led.plotBarGraph(input.acceleration(Dimension.X), 1023)
    x = input.acceleration(Dimension.X)
    if (x > 300) {
        music.changeTempoBy(20)
    }
    
})
