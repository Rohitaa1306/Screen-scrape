from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtWidgets import QLabel
from numpy import half


class MagnifyingLabel(QLabel):
    def __init__(self, parent=None):
        super(MagnifyingLabel, self).__init__(parent)
        self.gray_pen = QtGui.QPen(QtGui.QColor(128, 128, 128))
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self.parent().capture_click(event)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)

        if self.pixmap() is not None:
            magnify_size = 100
            magnification = 2

            x = event.pos().x()
            y = event.pos().y()

            pixmap = self.pixmap()

            half_size = magnify_size // (2 * magnification)

            if self.alignment() == Qt.AlignTop:
                top = y - half_size
                left = x - half_size
            # TODO elif self.alignment() == Qt.AlignCenter:
            else:
                raise ValueError(f"Invalid alignment {self.alignment()}, magnifying label will not work properly.")
 
            width = magnify_size // magnification
            height = magnify_size // magnification

            rect = QRect(left, top, width, height)
            magnified_pixmap = pixmap.copy(rect)
            magnified_pixmap = magnified_pixmap.scaled(magnify_size, magnify_size, Qt.KeepAspectRatio,
                                                       Qt.SmoothTransformation)

            final_pixmap = QPixmap(magnify_size, magnify_size)
            final_pixmap.fill(Qt.white)  # Fill the pixmap with white color

            x_offset = (magnify_size - magnified_pixmap.width()) // 2

            if x - half_size < 0:  # Cursor near the left edge
                x_offset = magnify_size - magnified_pixmap.width()
            elif x + half_size > pixmap.width():  # Cursor near the right edge
                x_offset = 0

            y_offset = (magnify_size - magnified_pixmap.height()) // 2  # Vertical offset remains centered

            if y - half_size < 0:  # Cursor near the left edge
                y_offset = magnify_size - magnified_pixmap.height()
            elif y + half_size > pixmap.height():  # Cursor near the right edge
                y_offset = 0

            painter = QPainter(final_pixmap)
            painter.drawPixmap(x_offset, y_offset, magnified_pixmap)
            painter.setPen(self.gray_pen)

            crosshair_x = magnify_size // 2
            crosshair_y = magnify_size // 2

            painter.drawLine(crosshair_x - 10, crosshair_y, crosshair_x + 10, crosshair_y)
            painter.drawLine(crosshair_x, crosshair_y - 10, crosshair_x, crosshair_y + 10)
            painter.end()

            self.parent().magnifier_label.setPixmap(final_pixmap)
            self.parent().magnifier_label.move(x, y)
