import time
import pygame
import pygame_gui
import random
from asset.Dictionary import Button

pygame.init()
pygame.display.set_caption("Rút bao lì xì")
screen = pygame.display.set_mode((1280, 720))
run = True
clock = pygame.time.Clock()

check_main = True
check_play = False
check_choose_value = False
check_shuffle = False

text_main = pygame.font.SysFont("Times New Roman", 100, True).render("RÚT BAO LÌ XÌ",
                                                                     True,
                                                                     "#FFFFFF")

text_play = pygame.font.SysFont("Times New Roman", 70, True).render("CHỌN SỐ LƯỢNG BAO LÌ XÌ",
                                                                    True,
                                                                    "#FFFFFF")

button_play = Button.Button_TEXT("Play",
                                 (None, 50),
                                 300,
                                 100,
                                 (screen.get_width() / 2 - 150, screen.get_height() / 2),
                                 (0, 255, 0),
                                 10)
button_play.border(border_thickness=10)

button_quit = Button.Button_TEXT("Quit",
                                 (None, 50),
                                 300,
                                 100,
                                 (screen.get_width() / 2 - 150, screen.get_height() / 2 + 150),
                                 (255, 0, 0),
                                 10)
button_quit.border(border_thickness=10)

button_return = Button.Button_TEXT("Return",
                                   (None, 50),
                                   200,
                                   100,
                                   (-25, -25),
                                   (50, 50, 50),
                                   30)

button_submit = Button.Button_TEXT("Submit",
                                   (None, 50),
                                   200,
                                   70,
                                   (screen.get_width() / 2 - 100, screen.get_height() / 2 + 100),
                                   (0, 255, 0),
                                   10)

button_submit2 = Button.Button_TEXT("Submit",
                                    (None, 50),
                                    200,
                                    70,
                                    (screen.get_width() / 2 + 200, screen.get_height() / 2 - 300),
                                    (0, 255, 0),
                                    10)

button_shuffle = Button.Button_TEXT("Shuffle",
                                    (None, 50),
                                    200,
                                    70,
                                    (screen.get_width() / 2 - 100, screen.get_height() / 2 - 300),
                                    (0, 255, 0),
                                    10)


def main():
    global run, check_main, check_play
    clock.tick(60)
    screen.fill((50, 50, 50))

    screen.blit(text_main, (screen.get_width() / 2 - text_main.get_width() / 2, text_main.get_height() - 50))

    if button_play.draw(screen):
        check_main = False
        check_play = True

    if button_quit.draw(screen):
        run = False


def play():
    global check_play, check_main, check_choose_value, run
    td = clock.tick(60) / 1000.0
    screen.fill((50, 50, 50))

    screen.blit(text_play, (screen.get_width() / 2 - text_play.get_width() / 2, text_play.get_height() - 20))

    if button_return.draw(screen):
        check_main = True
        check_play = False

    if button_submit.draw(screen):
        for i in range(1, int(drop_down.selected_option) + 1):
            exec(f"button_image2_baolixi{i}.enable_button()")
        else:
            for i in range(int(drop_down.selected_option) + 1, 7):
                exec(f"button_image2_baolixi{i}.disable_button()")

        check_play = False
        check_choose_value = True

    manager.update(td)
    manager.draw_ui(screen)


def choose_value():
    global check_play, check_choose_value, check_shuffle, mode
    td = clock.tick(60) / 1000.0
    screen.fill((50, 50, 50))

    if button_return.draw(screen):
        check_play = True
        check_choose_value = False

    if button_reset.draw(screen):
        for i in range(1, 7):
            exec(f"button_image2_baolixi{i}.value = 0")

    if button_submit2.draw(screen):
        for i in range(1, int(drop_down.selected_option) + 1):
            exec(f"button_image3_baolixi{i}.enable_button()")
        else:
            for i in range(int(drop_down.selected_option) + 1, 7):
                exec(f"button_image3_baolixi{i}.disable_button()")

        check_choose_value = False
        check_shuffle = True

    if mode:
        if button_plus.draw(screen):
            mode = False
    else:
        if button_minus.draw(screen):
            mode = True

    button_image_10k.draw(screen)
    button_image_20k.draw(screen)
    button_image_50k.draw(screen)
    button_image_100k.draw(screen)
    button_image_200k.draw(screen)
    button_image_500k.draw(screen)
    button_image2_baolixi1.draw(screen, td, mode)
    button_image2_baolixi2.draw(screen, td, mode)
    button_image2_baolixi3.draw(screen, td, mode)
    button_image2_baolixi4.draw(screen, td, mode)
    button_image2_baolixi5.draw(screen, td, mode)
    button_image2_baolixi6.draw(screen, td, mode)


def shuffle():
    global check_shuffle, check_choose_value, value, move, check_move, list_pos_button, list_pos_random
    td = clock.tick(60) / 1000.0
    screen.fill((50, 50, 50))

    if button_return.draw(screen):
        check_shuffle = False
        check_choose_value = True

    if button_shuffle.draw(screen) and not check_move:
        move = 0
        list_pos_random = list_pos_button.copy()
        random.shuffle(list_pos_random)
        check_move = True

    if check_move:
        move += 500 * td
        for i in range(6):
            if list_pos_button[i] < list_pos_random[i]:
                exec(
                    f"""if button_image3_baolixi{i + 1}.x >= list_pos_random[i]:\n    button_image3_baolixi{i + 1}.x = list_pos_random[i]\nelse:\n    button_image3_baolixi{i + 1}.x += move
                """)
            elif list_pos_button[i] > list_pos_random[i]:
                exec(
                    f"""if button_image3_baolixi{i + 1}.x <= list_pos_random[i]:\n    button_image3_baolixi{i + 1}.x = list_pos_random[i]\nelse:\n    button_image3_baolixi{i + 1}.x -= move
                """)

        if (button_image3_baolixi1.x == list_pos_random[0]
                and button_image3_baolixi2.x == list_pos_random[1]
                and button_image3_baolixi3.x == list_pos_random[2]
                and button_image3_baolixi4.x == list_pos_random[3]
                and button_image3_baolixi5.x == list_pos_random[4]
                and button_image3_baolixi6.x == list_pos_random[5]):
            list_pos_button = [button_image3_baolixi1.x, button_image3_baolixi2.x, button_image3_baolixi3.x,
                               button_image3_baolixi4.x, button_image3_baolixi5.x, button_image3_baolixi6.x]

            button_image3_baolixi1.image_rect.topleft = (button_image3_baolixi1.x, button_image3_baolixi1.y)
            button_image3_baolixi2.image_rect.topleft = (button_image3_baolixi2.x, button_image3_baolixi2.y)
            button_image3_baolixi3.image_rect.topleft = (button_image3_baolixi3.x, button_image3_baolixi3.y)
            button_image3_baolixi4.image_rect.topleft = (button_image3_baolixi4.x, button_image3_baolixi4.y)
            button_image3_baolixi5.image_rect.topleft = (button_image3_baolixi5.x, button_image3_baolixi5.y)
            button_image3_baolixi6.image_rect.topleft = (button_image3_baolixi6.x, button_image3_baolixi6.y)

            check_move = False

    if button_image3_baolixi1.draw(screen):
        button_image3_baolixi1.disable = True
        value = button_image2_baolixi1.value
    elif button_image3_baolixi2.draw(screen):
        button_image3_baolixi2.disable = True
        value = button_image2_baolixi2.value
    elif button_image3_baolixi3.draw(screen):
        button_image3_baolixi3.disable = True
        value = button_image2_baolixi3.value
    elif button_image3_baolixi4.draw(screen):
        button_image3_baolixi4.disable = True
        value = button_image2_baolixi4.value
    elif button_image3_baolixi5.draw(screen):
        button_image3_baolixi5.disable = True
        value = button_image2_baolixi5.value
    elif button_image3_baolixi6.draw(screen):
        button_image3_baolixi6.disable = True
        value = button_image2_baolixi6.value

    if value >= 0:
        text = pygame.font.SysFont("Times New Roman", 50, True).render(
            f"Số tiền ở trong bao lì xì là: {value}đ", True, "#00FF00")
        screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() / 2 - 150))


class Image_Button1:
    def __init__(self, x=0, y=0, image=None, space=0):
        self.x = x
        self.y = y
        self.image = image
        self.space = space
        self.clicked = False
        self.width = image.get_width()
        self.height = image.get_height()
        self.image_rect = image.get_rect()
        self.image_rect.topleft = (x, y)
        self.value = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x + self.value, self.y))
        return self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.image_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
            else:
                if self.clicked:
                    self.clicked = False
                    return True
            self.value = self.space
        else:
            self.value = 0
        return False

    def get_pos(self):
        return self.x


class Image_Button2:
    def __init__(self, x=0, y=0, image=None, space=0, disable=True, area=None):
        if area is None:
            area = []
        self.x = x
        self.y = y
        self.image = image
        self.space = space
        self.clicked_r = False
        self.clicked_s = False
        self.clicked_l = False
        self.clicked_rect = False
        self.width = image.get_width()
        self.height = image.get_height()
        self.image_rect = image.get_rect()
        self.image_rect.topleft = (x, y)
        self.value = 0
        self.value_space = 0
        self.disable = disable
        self.check = False
        self.check_time = False
        self.area = area
        self.active = False
        self.active_text = False
        self.text = pygame.font.SysFont("Times New Roman", 50, True).render(
            f"Số tiền ở trong bao lì xì là: {self.value}đ", True, "#00FF00")
        self.pos = 0
        self.image2 = pygame.surface.Surface((0, 0))
        self.list_image = [image_10k, image_20k, image_50k, image_100k, image_200k, image_500k]
        self.list_value = [10000, 20000, 50000, 100000, 200000, 500000]
        self.move = 0
        self.start = 0

    def draw(self, screen, td, mode):
        if not self.disable:
            if self.active:
                self.value_space = self.space
                self.image2 = pygame.transform.rotate(self.list_image[self.pos], 90)
                self.move += 200 * td
                if mode:
                    screen.blit(self.image2,
                                (self.x + self.width / 2 - self.image2.get_width() / 2,
                                 self.y - self.height + self.move))
                    if self.move >= self.y + self.height / 2 - self.image2.get_height() - self.space:
                        self.active = False
                        self.move = 0
                        self.value += self.list_value[self.pos]
                elif not mode and self.value - self.list_value[self.pos] >= 0:
                    screen.blit(self.image2,
                                (self.x + self.width / 2 - self.image2.get_width() / 2,
                                 self.y + self.height / 2 - self.image2.get_height() - self.space - self.move))
                    if self.y + self.height / 2 - self.image2.get_height() - self.space - self.move <= self.y - self.height:
                        self.active = False
                        self.move = 0
                        self.value -= self.list_value[self.pos]
                else:
                    self.active = False
                    self.move = 0
            if self.active_text:
                if not self.check_time:
                    self.text = pygame.font.SysFont("Times New Roman", 50, True).render(
                        f"Số tiền ở trong bao lì xì là: {self.value}đ", True, "#00FF00")
                    self.start = time.perf_counter()
                    self.check_time = True
                if time.perf_counter() - self.start >= 3:
                    self.active_text = False
                    self.check_time = False
                screen.blit(self.text, (screen.get_width() / 2 - self.text.get_width() / 2,
                                        screen.get_height() / 2 - self.text.get_height() / 2 - 100))
            screen.blit(self.image, (self.x, self.y - self.value_space))
            return self.check_click()

    def check_click(self):
        if not self.disable:
            mouse_pos = pygame.mouse.get_pos()
            if self.image_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.check = True
                    self.clicked_r = True
                elif pygame.mouse.get_pressed()[1]:
                    self.check = True
                    self.clicked_s = True
                elif pygame.mouse.get_pressed()[2]:
                    self.check = True
                    self.clicked_l = True
                else:
                    if self.clicked_r:
                        self.clicked_r = False
                        return True
                    if self.clicked_s:
                        self.clicked_s = False
                        self.active_text = True
                    if self.clicked_l:
                        self.clicked_l = False
                self.value_space = self.space
            if not self.check:
                self.value_space = 0
            elif not self.image_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    for pos, rect in enumerate(self.area):
                        if rect.collidepoint(mouse_pos) and not self.active:
                            self.pos = pos
                            self.clicked_rect = True
                            break
                    else:
                        self.check = False
                else:
                    if self.clicked_rect:
                        self.clicked_rect = False
                        self.active = True
                if self.active_text:
                    if pygame.mouse.get_pressed()[1]:
                        self.active_text = False
                        self.check_time = False
                        self.check = False
            return False

    def disable_button(self):
        self.disable = True

    def enable_button(self):
        self.disable = False


class Image_Button3:
    def __init__(self, x=0.0, y=0.0, image=None, space=0):
        self.x = x
        self.y = y
        self.image = image
        self.space = space
        self.value_space = 0
        self.clicked = False
        self.disable = False
        self.width = image.get_width()
        self.height = image.get_height()
        self.image_rect = image.get_rect()
        self.image_rect.topleft = (x, y)

    def draw(self, screen):
        if not self.disable:
            screen.blit(self.image, (self.x, self.y - self.value_space))
            return self.check_click()

    def check_click(self):
        if not self.disable:
            mouse_pos = pygame.mouse.get_pos()
            if self.image_rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                else:
                    if self.clicked:
                        self.clicked = False
                        return True
                self.value_space = self.space
            else:
                self.value_space = 0
            return False

    def disable_button(self):
        self.disable = True

    def enable_button(self):
        self.disable = False

    def get_pos(self):
        return self.x, self.y


scale = 0.5
image_10k = pygame.image.load("asset\\Image\\10k.jpg").convert_alpha()
image_10k = pygame.transform.smoothscale(image_10k, (image_10k.get_width() * scale, image_10k.get_height() * scale))
button_image_10k = Image_Button1(100, 100, image_10k, 50)

image_20k = pygame.image.load("asset\\Image\\20k.jpg").convert_alpha()
image_20k = pygame.transform.smoothscale(image_20k, (image_20k.get_width() * scale, image_20k.get_height() * scale))
button_image_20k = Image_Button1(100, 200, image_20k, 50)

image_50k = pygame.image.load("asset\\Image\\50k.jpg").convert_alpha()
image_50k = pygame.transform.smoothscale(image_50k, (image_50k.get_width() * scale, image_50k.get_height() * scale))
button_image_50k = Image_Button1(100, 300, image_50k, 50)

image_100k = pygame.image.load("asset\\Image\\100k.jpg").convert_alpha()
image_100k = pygame.transform.smoothscale(image_100k, (image_100k.get_width() * scale, image_100k.get_height() * scale))
button_image_100k = Image_Button1(100, 400, image_100k, 50)

image_200k = pygame.image.load("asset\\Image\\200k.jpg").convert_alpha()
image_200k = pygame.transform.smoothscale(image_200k, (image_200k.get_width() * scale, image_200k.get_height() * scale))
button_image_200k = Image_Button1(100, 500, image_200k, 50)

image_500k = pygame.image.load("asset\\Image\\500k.jpg").convert_alpha()
image_500k = pygame.transform.smoothscale(image_500k, (image_500k.get_width() * scale, image_500k.get_height() * scale))
button_image_500k = Image_Button1(100, 600, image_500k, 50)

image_baolixi = pygame.image.load("asset\\Image\\baolixi.jpg").convert_alpha()
image_baolixi = pygame.transform.smoothscale(image_baolixi,
                                             (image_baolixi.get_width() * 0.25, image_baolixi.get_height() * 0.25))

area = [button_image_10k.image_rect, button_image_20k.image_rect, button_image_50k.image_rect,
        button_image_100k.image_rect, button_image_200k.image_rect, button_image_500k.image_rect]

button_image2_baolixi1 = Image_Button2(375, 400, image_baolixi, 50, area=area)
button_image2_baolixi2 = Image_Button2(525, 400, image_baolixi, 50, area=area)
button_image2_baolixi3 = Image_Button2(675, 400, image_baolixi, 50, area=area)
button_image2_baolixi4 = Image_Button2(825, 400, image_baolixi, 50, area=area)
button_image2_baolixi5 = Image_Button2(975, 400, image_baolixi, 50, area=area)
button_image2_baolixi6 = Image_Button2(1125, 400, image_baolixi, 50, area=area)

x = screen.get_width() / 6
space = (x - image_baolixi.get_width()) / 2
button_image3_baolixi1 = Image_Button3(x * 0 + space, 400, image_baolixi, 50)
button_image3_baolixi2 = Image_Button3(x * 1 + space, 400, image_baolixi, 50)
button_image3_baolixi3 = Image_Button3(x * 2 + space, 400, image_baolixi, 50)
button_image3_baolixi4 = Image_Button3(x * 3 + space, 400, image_baolixi, 50)
button_image3_baolixi5 = Image_Button3(x * 4 + space, 400, image_baolixi, 50)
button_image3_baolixi6 = Image_Button3(x * 5 + space, 400, image_baolixi, 50)

button_plus = Button.Button_TEXT("+",
                                 (None, 40),
                                 50,
                                 40,
                                 (screen.get_width() / 2 - 300, screen.get_height() / 4 - 100),
                                 (0, 255, 0),
                                 10)

button_minus = Button.Button_TEXT("-",
                                  (None, 40),
                                  50,
                                  40,
                                  (screen.get_width() / 2 - 300, screen.get_height() / 4 - 100),
                                  (255, 0, 0),
                                  10)

button_reset = Button.Button_TEXT("RESET",
                                  (None, 35),
                                  100,
                                  50,
                                  (screen.get_width() / 2 - 300, screen.get_height() / 4 - 150),
                                  (255, 0, 0),
                                  10)

active = False
value = -1
mode = True
move = 0
check_move = False
list_pos_button = [button_image3_baolixi1.x, button_image3_baolixi2.x, button_image3_baolixi3.x,
                   button_image3_baolixi4.x, button_image3_baolixi5.x, button_image3_baolixi6.x]
list_pos_random = []

manager = pygame_gui.UIManager(screen.get_size())

drop_down = pygame_gui.elements.UIDropDownMenu(options_list=["1", "2", "3", "4", "5", "6"],
                                               starting_option="1",
                                               relative_rect=pygame.Rect(screen.get_width() / 2 - 150,
                                                                         screen.get_height() / 2 - 125, 300, 50)
                                               )

label = pygame.font.Font(None, 20).render("Left|Scroll|Right", True, "#FFFFFF")

while run:
    events = pygame.event.get()

    if check_main:
        main()
    elif check_play:
        play()
    elif check_choose_value:
        choose_value()
    elif check_shuffle:
        shuffle()

    fps_screen = pygame.font.Font(None, 30).render("FPS {}".format(int(clock.get_fps())), True, (255, 255, 255))
    rect_fps = pygame.rect.Rect(0, screen.get_height() - 20, fps_screen.get_width(), fps_screen.get_height())
    screen.blit(fps_screen, (0, screen.get_height() - 20))

    click = pygame.mouse.get_pressed()
    click = [str(i) for i in click]
    click_label = pygame.font.Font(None, 20).render("{}".format(" ".join(click)), True, "#FFFFFF")
    screen.blit(label, (screen.get_width() - label.get_width(), 7))
    screen.blit(click_label, (screen.get_width() - click_label.get_width(), 20))

    for event in events:
        if event.type == pygame.QUIT:
            run = False
        manager.process_events(event)

    pygame.display.flip()
