import simpleaudio as sa

AUDIO_PATH = "/home/pi/ecse211/project-t08/project/audio/"

if __name__ == "__main__":
    file_path = AUDIO_PATH + "twenty.wav"
    print(file_path)
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

    file_path = AUDIO_PATH + "report.wav"
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()