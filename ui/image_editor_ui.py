# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_editor_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ImageEditor(object):
    def setupUi(self, ImageEditor):
        ImageEditor.setObjectName("ImageEditor")
        ImageEditor.resize(357, 508)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ImageEditor.sizePolicy().hasHeightForWidth())
        ImageEditor.setSizePolicy(sizePolicy)
        ImageEditor.setMinimumSize(QtCore.QSize(357, 508))
        ImageEditor.setMaximumSize(QtCore.QSize(357, 508))
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(ImageEditor)
        self.horizontalLayout_18.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.line_9 = QtWidgets.QFrame(ImageEditor)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.horizontalLayout_18.addWidget(self.line_9)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.line_3 = QtWidgets.QFrame(ImageEditor)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_8.addWidget(self.line_3)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.image_editor_label = QtWidgets.QLabel(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_editor_label.sizePolicy().hasHeightForWidth())
        self.image_editor_label.setSizePolicy(sizePolicy)
        self.image_editor_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_editor_label.setObjectName("image_editor_label")
        self.horizontalLayout_27.addWidget(self.image_editor_label)
        self.verticalLayout_8.addLayout(self.horizontalLayout_27)
        self.line_11 = QtWidgets.QFrame(ImageEditor)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.verticalLayout_8.addWidget(self.line_11)
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.input_folder_label = QtWidgets.QLabel(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_folder_label.sizePolicy().hasHeightForWidth())
        self.input_folder_label.setSizePolicy(sizePolicy)
        self.input_folder_label.setObjectName("input_folder_label")
        self.horizontalLayout_29.addWidget(self.input_folder_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_29.addItem(spacerItem)
        self.verticalLayout_8.addLayout(self.horizontalLayout_29)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.input_file_line_edit = QtWidgets.QLineEdit(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_file_line_edit.sizePolicy().hasHeightForWidth())
        self.input_file_line_edit.setSizePolicy(sizePolicy)
        self.input_file_line_edit.setMinimumSize(QtCore.QSize(184, 25))
        self.input_file_line_edit.setMaximumSize(QtCore.QSize(184, 25))
        self.input_file_line_edit.setText("")
        self.input_file_line_edit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.input_file_line_edit.setObjectName("input_file_line_edit")
        self.horizontalLayout_28.addWidget(self.input_file_line_edit)
        self.input_file_browser = QtWidgets.QToolButton(ImageEditor)
        self.input_file_browser.setMinimumSize(QtCore.QSize(65, 27))
        self.input_file_browser.setMaximumSize(QtCore.QSize(65, 27))
        self.input_file_browser.setObjectName("input_file_browser")
        self.horizontalLayout_28.addWidget(self.input_file_browser)
        self.verticalLayout_8.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_55 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_55.setObjectName("horizontalLayout_55")
        self.save_as_label = QtWidgets.QLabel(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_as_label.sizePolicy().hasHeightForWidth())
        self.save_as_label.setSizePolicy(sizePolicy)
        self.save_as_label.setObjectName("save_as_label")
        self.horizontalLayout_55.addWidget(self.save_as_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_55.addItem(spacerItem1)
        self.verticalLayout_8.addLayout(self.horizontalLayout_55)
        self.horizontalLayout_56 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_56.setObjectName("horizontalLayout_56")
        self.save_as_line_edit = QtWidgets.QLineEdit(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_as_line_edit.sizePolicy().hasHeightForWidth())
        self.save_as_line_edit.setSizePolicy(sizePolicy)
        self.save_as_line_edit.setMinimumSize(QtCore.QSize(184, 25))
        self.save_as_line_edit.setMaximumSize(QtCore.QSize(184, 25))
        self.save_as_line_edit.setText("")
        self.save_as_line_edit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.save_as_line_edit.setObjectName("save_as_line_edit")
        self.horizontalLayout_56.addWidget(self.save_as_line_edit)
        self.save_as_browser = QtWidgets.QToolButton(ImageEditor)
        self.save_as_browser.setMinimumSize(QtCore.QSize(65, 27))
        self.save_as_browser.setMaximumSize(QtCore.QSize(65, 27))
        self.save_as_browser.setObjectName("save_as_browser")
        self.horizontalLayout_56.addWidget(self.save_as_browser)
        self.verticalLayout_8.addLayout(self.horizontalLayout_56)
        self.line_2 = QtWidgets.QFrame(ImageEditor)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_8.addWidget(self.line_2)
        self.horizontalLayout_51 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_51.setObjectName("horizontalLayout_51")
        self.frame = QtWidgets.QFrame(ImageEditor)
        self.frame.setMinimumSize(QtCore.QSize(192, 108))
        self.frame.setMaximumSize(QtCore.QSize(192, 108))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(5)
        self.frame.setMidLineWidth(3)
        self.frame.setObjectName("frame")
        self.img_widget = QtWidgets.QLabel(self.frame)
        self.img_widget.setGeometry(QtCore.QRect(0, 0, 192, 108))
        self.img_widget.setText("")
        self.img_widget.setAlignment(QtCore.Qt.AlignCenter)
        self.img_widget.setObjectName("img_widget")
        self.horizontalLayout_51.addWidget(self.frame)
        self.verticalLayout_8.addLayout(self.horizontalLayout_51)
        self.line_5 = QtWidgets.QFrame(ImageEditor)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_8.addWidget(self.line_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.select_size_label = QtWidgets.QLabel(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_size_label.sizePolicy().hasHeightForWidth())
        self.select_size_label.setSizePolicy(sizePolicy)
        self.select_size_label.setMinimumSize(QtCore.QSize(80, 0))
        self.select_size_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.select_size_label.setObjectName("select_size_label")
        self.horizontalLayout_6.addWidget(self.select_size_label)
        spacerItem2 = QtWidgets.QSpacerItem(94, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.size_dropdown = QtWidgets.QComboBox(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.size_dropdown.sizePolicy().hasHeightForWidth())
        self.size_dropdown.setSizePolicy(sizePolicy)
        self.size_dropdown.setMinimumSize(QtCore.QSize(75, 25))
        self.size_dropdown.setMaximumSize(QtCore.QSize(75, 25))
        self.size_dropdown.setObjectName("size_dropdown")
        self.horizontalLayout_6.addWidget(self.size_dropdown)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.line_4 = QtWidgets.QFrame(ImageEditor)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_8.addWidget(self.line_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.preset_filter_label = QtWidgets.QLabel(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_filter_label.sizePolicy().hasHeightForWidth())
        self.preset_filter_label.setSizePolicy(sizePolicy)
        self.preset_filter_label.setMinimumSize(QtCore.QSize(80, 0))
        self.preset_filter_label.setMaximumSize(QtCore.QSize(80, 16777215))
        self.preset_filter_label.setObjectName("preset_filter_label")
        self.horizontalLayout_10.addWidget(self.preset_filter_label)
        spacerItem3 = QtWidgets.QSpacerItem(94, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.preset_filter_dropdown = QtWidgets.QComboBox(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preset_filter_dropdown.sizePolicy().hasHeightForWidth())
        self.preset_filter_dropdown.setSizePolicy(sizePolicy)
        self.preset_filter_dropdown.setMinimumSize(QtCore.QSize(75, 25))
        self.preset_filter_dropdown.setMaximumSize(QtCore.QSize(75, 25))
        self.preset_filter_dropdown.setObjectName("preset_filter_dropdown")
        self.horizontalLayout_10.addWidget(self.preset_filter_dropdown)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.filter_label = QtWidgets.QLabel(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_label.sizePolicy().hasHeightForWidth())
        self.filter_label.setSizePolicy(sizePolicy)
        self.filter_label.setMinimumSize(QtCore.QSize(80, 0))
        self.filter_label.setMaximumSize(QtCore.QSize(97, 16777215))
        self.filter_label.setObjectName("filter_label")
        self.horizontalLayout_8.addWidget(self.filter_label)
        spacerItem4 = QtWidgets.QSpacerItem(77, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.filter_dropdown = QtWidgets.QComboBox(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_dropdown.sizePolicy().hasHeightForWidth())
        self.filter_dropdown.setSizePolicy(sizePolicy)
        self.filter_dropdown.setMinimumSize(QtCore.QSize(75, 25))
        self.filter_dropdown.setMaximumSize(QtCore.QSize(75, 25))
        self.filter_dropdown.setObjectName("filter_dropdown")
        self.horizontalLayout_8.addWidget(self.filter_dropdown)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_49 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_49.setObjectName("horizontalLayout_49")
        self.kernel_size_label = QtWidgets.QLabel(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kernel_size_label.sizePolicy().hasHeightForWidth())
        self.kernel_size_label.setSizePolicy(sizePolicy)
        self.kernel_size_label.setMinimumSize(QtCore.QSize(145, 0))
        self.kernel_size_label.setMaximumSize(QtCore.QSize(145, 16777215))
        self.kernel_size_label.setObjectName("kernel_size_label")
        self.horizontalLayout_49.addWidget(self.kernel_size_label)
        spacerItem5 = QtWidgets.QSpacerItem(39, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_49.addItem(spacerItem5)
        self.kernel_size_entry = QtWidgets.QLineEdit(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kernel_size_entry.sizePolicy().hasHeightForWidth())
        self.kernel_size_entry.setSizePolicy(sizePolicy)
        self.kernel_size_entry.setMinimumSize(QtCore.QSize(65, 25))
        self.kernel_size_entry.setMaximumSize(QtCore.QSize(65, 25))
        self.kernel_size_entry.setText("")
        self.kernel_size_entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.kernel_size_entry.setObjectName("kernel_size_entry")
        self.horizontalLayout_49.addWidget(self.kernel_size_entry)
        self.verticalLayout_8.addLayout(self.horizontalLayout_49)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.apply_button = QtWidgets.QPushButton(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_button.sizePolicy().hasHeightForWidth())
        self.apply_button.setSizePolicy(sizePolicy)
        self.apply_button.setMinimumSize(QtCore.QSize(80, 27))
        self.apply_button.setMaximumSize(QtCore.QSize(80, 27))
        self.apply_button.setObjectName("apply_button")
        self.horizontalLayout_7.addWidget(self.apply_button)
        spacerItem6 = QtWidgets.QSpacerItem(169, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.message_label = QtWidgets.QLabel(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_label.sizePolicy().hasHeightForWidth())
        self.message_label.setSizePolicy(sizePolicy)
        self.message_label.setMinimumSize(QtCore.QSize(0, 20))
        self.message_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.message_label.setText("")
        self.message_label.setObjectName("message_label")
        self.horizontalLayout_7.addWidget(self.message_label)
        spacerItem7 = QtWidgets.QSpacerItem(169, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.line = QtWidgets.QFrame(ImageEditor)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_8.addWidget(self.line)
        self.horizontalLayout_68 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_68.setObjectName("horizontalLayout_68")
        self.save_button = QtWidgets.QPushButton(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setMinimumSize(QtCore.QSize(80, 27))
        self.save_button.setMaximumSize(QtCore.QSize(80, 27))
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_68.addWidget(self.save_button)
        self.back_button = QtWidgets.QPushButton(ImageEditor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setMinimumSize(QtCore.QSize(80, 27))
        self.back_button.setMaximumSize(QtCore.QSize(80, 27))
        self.back_button.setObjectName("back_button")
        self.horizontalLayout_68.addWidget(self.back_button)
        self.verticalLayout_8.addLayout(self.horizontalLayout_68)
        spacerItem9 = QtWidgets.QSpacerItem(20, 1, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_8.addItem(spacerItem9)
        self.line_12 = QtWidgets.QFrame(ImageEditor)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.verticalLayout_8.addWidget(self.line_12)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_4)
        self.line_13 = QtWidgets.QFrame(ImageEditor)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.horizontalLayout_18.addWidget(self.line_13)

        self.retranslateUi(ImageEditor)
        QtCore.QMetaObject.connectSlotsByName(ImageEditor)

    def retranslateUi(self, ImageEditor):
        _translate = QtCore.QCoreApplication.translate
        ImageEditor.setWindowTitle(_translate("ImageEditor", "𝕀mage𝔼vo"))
        self.image_editor_label.setText(_translate("ImageEditor", "Image Editor"))
        self.input_folder_label.setToolTip(_translate("ImageEditor", "The input file path (supported types: jpg, jpeg, jpe, jfif, png)"))
        self.input_folder_label.setText(_translate("ImageEditor", "Image file:"))
        self.input_file_line_edit.setToolTip(_translate("ImageEditor", "The input file path (supported types: jpg, jpeg, jpe, jfif, png)"))
        self.input_file_browser.setToolTip(_translate("ImageEditor", "Browse for input file (supported types: jpg, jpeg, jpe, jfif, png)"))
        self.input_file_browser.setText(_translate("ImageEditor", "..."))
        self.save_as_label.setToolTip(_translate("ImageEditor", "The folder in which to output images"))
        self.save_as_label.setText(_translate("ImageEditor", "Save as"))
        self.save_as_line_edit.setToolTip(_translate("ImageEditor", "<html><head/><body><p>Where should the edited image be saved?</p></body></html>"))
        self.save_as_browser.setToolTip(_translate("ImageEditor", "<html><head/><body><p>Where should the edited image be saved?</p></body></html>"))
        self.save_as_browser.setText(_translate("ImageEditor", "..."))
        self.select_size_label.setText(_translate("ImageEditor", "Resize size"))
        self.size_dropdown.setToolTip(_translate("ImageEditor", "<html><head/><body><p>The length of the largest image dimension in pixels. Each size corresponds easily to bit lengths.</p></body></html>"))
        self.preset_filter_label.setText(_translate("ImageEditor", "Preset filters"))
        self.preset_filter_dropdown.setToolTip(_translate("ImageEditor", "<html><head/><body><p>Preset Python PIL filters.</p></body></html>"))
        self.filter_label.setText(_translate("ImageEditor", "Custom Filter"))
        self.filter_dropdown.setToolTip(_translate("ImageEditor", "<html><head/><body><p>Python PIL filters that have require a size argument. </p></body></html>"))
        self.kernel_size_label.setToolTip(_translate("ImageEditor", "How much to weight the global best position during crossover"))
        self.kernel_size_label.setText(_translate("ImageEditor", "Filter size argument"))
        self.kernel_size_entry.setToolTip(_translate("ImageEditor", "<html><head/><body><p>Depending on the filter that is currently selected, this value may correspond to kernel size in pixels or radius.</p></body></html>"))
        self.apply_button.setToolTip(_translate("ImageEditor", "Return to previous screen"))
        self.apply_button.setText(_translate("ImageEditor", "Apply"))
        self.save_button.setToolTip(_translate("ImageEditor", "Return to previous screen"))
        self.save_button.setText(_translate("ImageEditor", "Save"))
        self.back_button.setToolTip(_translate("ImageEditor", "Execute the algorithm"))
        self.back_button.setText(_translate("ImageEditor", "Back"))
