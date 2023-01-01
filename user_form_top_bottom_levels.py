# -*- coding: utf-8 -*-
import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')

import System
import System.Drawing
import System.Windows.Forms


class UserFormTopBottomLevels(System.Windows.Forms.Form):
    def __init__(self):
        self.Text = "Перечислите номера групп исключаемых из стояка"
        self.BackColor = System.Drawing.Color.FromArgb(238, 238, 238)
        caption_height = System.Windows.Forms.SystemInformation.CaptionHeight
        self.MinimumSize = System.Drawing.Size(550, (700 + caption_height))
        self.CenterToScreen()

        self._label_font = System.Drawing.Font(
                                        'Arial',
                                        System.Single(10.5),
                                        System.Drawing.FontStyle.Regular,
                                        System.Drawing.GraphicsUnit.Point)

        self._label_comment_stair = System.Windows.Forms.Label()
        self._label_comment_stair.Text = 'Укажите в строке ниже, номера групп,\
                                        \nкоторые ИДУТ ВНЕ СТОЯКА, например ПО ЛЕСТНИЦАМ.\
                                        \nЗапишите через запятую, без пробелов, в следующем виде: 1,12,1А,4,9А\
                                        \nСокращение гр. к каждой группе писать не надо, только номер.'
        self._label_comment_stair.Font = self._label_font
        self._label_comment_stair.Location = System.Drawing.Point(20, 5)
        self._label_comment_stair.Size = System.Drawing.Size(
            self._label_comment_stair.PreferredWidth, self._label_comment_stair.PreferredHeight)
        self.Controls.Add(self._label_comment_stair)

        self._text_box_stair = System.Windows.Forms.TextBox()
        self._text_box_stair.Location = System.Drawing.Point(20, 80)
        self._text_box_stair.Size = System.Drawing.Size(400, 100)
        self.Controls.Add(self._text_box_stair)

        self._label_info_stair = System.Windows.Forms.Label()
        self._label_info_stair.Text = '  Для напоминания.\
                                    \nОбычно в проектах вне стояка идут:\
                                    \nгр.1А - освещение лестничных переходов\
                                    \nгр.7А - освещение подъема на 1 этаж с подвала, СУВ\
                                    \nгр.9 - освещение входа с улицы в подвал, выключатель при входе\
                                    \nгр.9А - освещение освновной лестничной клетки\
                                    \nгр.11А - освещение освновной лестничной клетки\
                                    \nгр.15А - освещение дополнительной лестничной клетки\
                                    \nгр.16А - освещение дополнительной лестничной клетки'
        self._label_info_stair.Font = self._label_font
        self._label_info_stair.Location = System.Drawing.Point(40, 110)
        self._label_info_stair.Size = System.Drawing.Size(
            self._label_info_stair.PreferredWidth, self._label_info_stair.PreferredHeight)
        self.Controls.Add(self._label_info_stair)


        self.offset = 400

        self._label_exclude = System.Windows.Forms.Label()
        self._label_exclude.Text = 'Вариант для двух стояков в здании.\
                                        \nИСКЛЮЧИТЬ ГРУППЫ ИЗ ПРАВОГО/ВТОРОГО СТОЯКА.\
                                        \nЗапишите через запятую, без пробелов, в следующем виде: 16,18\
                                        \nСокращение гр. к каждой группе писать не надо, только номер.'
        self._label_exclude.Font = self._label_font
        self._label_exclude.Location = System.Drawing.Point(20, 5 + self.offset)
        self._label_exclude.Size = System.Drawing.Size(
            self._label_exclude.PreferredWidth, self._label_exclude.PreferredHeight)
        self.Controls.Add(self._label_exclude)

        self._text_box_exclude = System.Windows.Forms.TextBox()
        self._text_box_exclude.Location = System.Drawing.Point(20, 80 + self.offset)
        self._text_box_exclude.Size = System.Drawing.Size(400,100)
        self.Controls.Add(self._text_box_exclude)

        self._label_info_exclude = System.Windows.Forms.Label()
        self._label_info_exclude.Text = '  Для примера:\
                                    \nнапример, гр.16 - на первом этаже из-за сложного ветвления\
                                    \nпопала в баундингбокс, в то время,\
                                    \nкак идет она в стояке, который вне баундингбокса'
        self._label_info_exclude.Font = self._label_font
        self._label_info_exclude.Location = System.Drawing.Point(30, 110 + self.offset)
        self._label_info_exclude.Size = System.Drawing.Size(
            self._label_info_exclude.PreferredWidth, self._label_info_exclude.PreferredHeight)
        self.Controls.Add(self._label_info_exclude)







# # для Dynamo
# f = Window()  # создали экземпляр класса Window
# if f.ShowDialog() == DialogResult.OK:
#     # из строки сделали список строк
#     OUT = ['гр.' + let for let in f.input_str().split (',')]

# для RPS, в Dynamo это условие не будет выполняться
# if __name__ == "__main__":
f = UserFormTopBottomLevels() #создали экземпляр класса Window, экземпляр формы
f.ShowDialog() #чтоб при запуске данная форма появилась
