def on_forever():
    serial.write_value("earthquake", pins.analog_read_pin(AnalogPin.P1))
    serial.write_value("level", pins.analog_read_pin(AnalogPin.P0))
    serial.write_value("fire", pins.analog_read_pin(AnalogPin.P2))
    serial.write_value("gas", pins.analog_read_pin(AnalogPin.P3))
    basic.show_number(pins.analog_read_pin(AnalogPin.P1))
    basic.show_number(pins.analog_read_pin(AnalogPin.P0))
    basic.show_number(pins.analog_read_pin(AnalogPin.P2))
    basic.show_number(pins.analog_read_pin(AnalogPin.P3))
basic.forever(on_forever)

def on_forever2():
    if pins.analog_read_pin(AnalogPin.P1) >= 1004 and (pins.analog_read_pin(AnalogPin.P0) <= 300 and (pins.analog_read_pin(AnalogPin.P2) == 1 and pins.analog_read_pin(AnalogPin.P3) >= 40)):
        pins.digital_write_pin(DigitalPin.P0, 1)
        basic.show_number(1)
        music.play_melody("G F E B D C C5 G ", 500)
        basic.pause(2000)
    pins.digital_write_pin(DigitalPin.P0, 0)
    basic.show_number(0)
basic.forever(on_forever2)
