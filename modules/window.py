from PyQt6.QtWidgets import QMainWindow, QFrame, QHBoxLayout, QVBoxLayout, QLabel, QGridLayout
from modules.app import app
from PyQt6.QtCore import Qt



main_window = QMainWindow()



WIDTH_WINDOW = 1024
HEIGHT_WINDOW = 800

primary_screen = app.primaryScreen()
screen_size = primary_screen.size()
width_screen = screen_size.width()
height_screen = screen_size.height()


main_window.setGeometry(
    (width_screen // 2) - (WIDTH_WINDOW // 2), 
    (height_screen // 2) - (HEIGHT_WINDOW // 2), 
    WIDTH_WINDOW, 
    HEIGHT_WINDOW
)

# frame = QFrame(mai)

# frame_1 = QFrame(parent= frame)

main_frame = QFrame(main_window)
main_frame.setStyleSheet("background-color: grey")
main_frame.setFixedSize(WIDTH_WINDOW, HEIGHT_WINDOW)
main_layout = QVBoxLayout(main_frame)

big_frame = QFrame(main_window)
big_frame.setStyleSheet("background-color: grey")
big_frame.setFixedSize(WIDTH_WINDOW, 250) 
main_layout.addWidget(big_frame) 

big_frame1 = QFrame(main_window)
big_frame1.setStyleSheet("background-color: grey") 
big_frame1.setFixedSize(WIDTH_WINDOW, 250) 
main_layout.addWidget(big_frame1)

big_frame2 = QFrame(main_window)
big_frame2.setStyleSheet("background-color: grey") 
big_frame2.setFixedSize(WIDTH_WINDOW, 250)
main_layout.addWidget(big_frame2) 



frame_layout1 = QHBoxLayout(big_frame)
frame_layout2 = QHBoxLayout(big_frame1)
frame_layout3 = QHBoxLayout(big_frame2)

frame_red1 = QFrame(big_frame)
frame_red1.setStyleSheet("background-color: red")
frame_red1.setFixedSize(325, 255)
frame_layout1.addWidget(frame_red1)

frame_red2 = QFrame(big_frame)
frame_red2.setStyleSheet("background-color: red")
frame_red2.setFixedSize(325, 255)
frame_layout1.addWidget(frame_red2)

frame_red3 = QFrame(big_frame)
frame_red3.setStyleSheet("background-color: red")
frame_red3.setFixedSize(325, 255)
frame_layout1.addWidget(frame_red3)


frame_green1 = QFrame(big_frame1)
frame_green1.setStyleSheet("background-color: green")
frame_green1.setFixedSize(325, 255)
frame_layout2.addWidget(frame_green1)

frame_green2 = QFrame(big_frame1)
frame_green2.setStyleSheet("background-color: green")
frame_green2.setFixedSize(325, 255)
frame_layout2.addWidget(frame_green2)

frame_green3 = QFrame(big_frame1)
frame_green3.setStyleSheet("background-color: green")
frame_green3.setFixedSize(325, 255)
frame_layout2.addWidget(frame_green3)

frame_blue1 = QFrame(big_frame2)
frame_blue1.setStyleSheet("background-color: blue")
frame_blue1.setFixedSize(325, 255)
frame_layout3.addWidget(frame_blue1)

frame_blue2 = QFrame(big_frame2)
frame_blue2.setStyleSheet("background-color: blue")
frame_blue2.setFixedSize(325, 255)
frame_layout3.addWidget(frame_blue2)

frame_blue3 = QFrame(big_frame2)
frame_blue3.setStyleSheet("background-color: blue")
frame_blue3.setFixedSize(325, 255)
frame_layout3.addWidget(frame_blue3)



small_square_layout1 = QHBoxLayout(frame_red1)
small_square_layout3 = QHBoxLayout(frame_red3)
small_square_layout1_ = QHBoxLayout(frame_blue1)
small_square_layout3_ = QHBoxLayout(frame_blue3)



sqruare_white = QFrame(frame_red1)
sqruare_white.setStyleSheet("background-color: white")
sqruare_white.setFixedSize(40,40)
small_square_layout1.addWidget(sqruare_white)

sqruare_grey = QFrame(frame_red1)
sqruare_grey.setStyleSheet("background-color: grey")
sqruare_grey.setFixedSize(40,40)
small_square_layout1.addWidget(sqruare_grey)

sqruare_white2 = QFrame(frame_red3)
sqruare_white2.setStyleSheet("background-color: white")
sqruare_white2.setFixedSize(40,40)
small_square_layout3.addWidget(sqruare_white2)

sqruare_grey2 = QFrame(frame_red1)
sqruare_grey2.setStyleSheet("background-color: grey")
sqruare_grey2.setFixedSize(40,40)
small_square_layout3.addWidget(sqruare_grey2)

sqruare_white3 = QFrame(frame_blue1)
sqruare_white3.setStyleSheet("background-color: white")
sqruare_white3.setFixedSize(40,40)
small_square_layout1_.addWidget(sqruare_white3)

sqruare_grey3 = QFrame(frame_blue1)
sqruare_grey3.setStyleSheet("background-color: grey")
sqruare_grey3.setFixedSize(40,40)
small_square_layout1_.addWidget(sqruare_grey3)

sqruare_white4 = QFrame(frame_blue3)
sqruare_white4.setStyleSheet("background-color: white")
sqruare_white4.setFixedSize(40,40)
small_square_layout3_.addWidget(sqruare_white4)

sqruare_grey4 = QFrame(frame_blue3)
sqruare_grey4.setStyleSheet("background-color: grey")
sqruare_grey4.setFixedSize(40,40)
small_square_layout3_.addWidget(sqruare_grey4)




green_layout1 = QVBoxLayout(frame_green1)
green_layout2 = QVBoxLayout(frame_green2)
green_layout3 = QVBoxLayout(frame_green3)


label1 = QLabel(parent=frame_green1, text= "Лейбл1")
green_layout1.setAlignment(Qt.AlignmentFlag.AlignCenter)
green_layout1.addWidget(label1)

label2 = QLabel(parent=frame_green1, text= "Лейбл2")
green_layout1.setAlignment(Qt.AlignmentFlag.AlignCenter)
green_layout1.addWidget(label2)

label3 = QLabel(parent=frame_green2, text= "Лейбл1")
green_layout2.setAlignment(Qt.AlignmentFlag.AlignCenter)
green_layout2.addWidget(label3)

label4 = QLabel(parent=frame_green2, text= "Лейбл2")
green_layout2.setAlignment(Qt.AlignmentFlag.AlignCenter)
green_layout2.addWidget(label4)

label5 = QLabel(parent=frame_green3, text= "Лейбл1")
green_layout3.setAlignment(Qt.AlignmentFlag.AlignCenter)
green_layout3.addWidget(label5)

label6 = QLabel(parent=frame_green3, text= "Лейбл2")
green_layout3.setAlignment(Qt.AlignmentFlag.AlignCenter)
green_layout3.addWidget(label6)











