class Video():
    def __init__(self, video_title, video_duration, video_storyline,):
        self.title = video_title
        self.duration = video_duration
        self.storyline = video_storyline

    def show_info(self):
        print('Title: ' + self.title)
        print('Duration: ' + self.duration)
        print('Storyline: ' + self.storyline)