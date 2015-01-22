# -*- coding: utf-8 -*-
from copy import copy
from fpdf import FPDF, HTMLMixin

from django.http import HttpResponse
from django.utils import six
from django.utils.translation import ugettext_lazy as _

from . import colors


class FPDF_HTML(FPDF, HTMLMixin):
    def vertical_line(self, x, y, length, color=None, weight=1, style='solid'):
        self.line(x, y, x, y+length, color=color, weight=weight, style=style)

    def horizontal_line(self, x, y, length, color=None, weight=1, style='solid'):
        self.line(x, y, x+length, y, color=color, weight=weight, style=style)

    def set_text_color(self, r, g=-1, b=-1):
        self.old_text_color = self.text_color
        super(FPDF_HTML, self).set_text_color(r, g, b)

    def restore_text_color(self):
        try:
            self.text_color = self.old_text_color
        except AttributeError:
            pass

    def set_fill_color(self, r, g=-1, b=-1):
        self.old_fill_color = self.fill_color
        super(FPDF_HTML, self).set_fill_color(r, g, b)

    def restore_fill_color(self):
        try:
            self.fill_color = self.old_fill_color
        except AttributeError:
            pass

    def set_draw_color(self, r, g=-1, b=-1):
        self.old_draw_color = self.draw_color
        super(FPDF_HTML, self).set_draw_color(r, g, b)

    def restore_draw_color(self):
        try:
            self.draw_color = self.old_draw_color
        except AttributeError:
            pass

    def line(self, x1, y1, x2, y2, color=None, weight=1, style='solid'):
        if color is not None:
            self.set_draw_color(*color)

        if x1 == x2:
            # vertical
            for line in range(1, weight+1, 1):
                if style == 'dashed':
                    super(FPDF_HTML, self).dashed_line(x1 + (line - 1)*0.2, y1, x2 + (line - 1)*0.2, y2)
                else:
                    super(FPDF_HTML, self).line(x1 + (line - 1)*0.2, y1, x2 + (line - 1)*0.2, y2)

        elif y1 == y2:
            # horizontal
            for line in range(1, weight+1, 1):
                if style == 'dashed':
                    super(FPDF_HTML, self).dashed_line(x1, y1 + (line - 1)*0.2, x2, y2 + (line - 1)*0.2)
                else:
                    super(FPDF_HTML, self).line(x1, y1 + (line - 1)*0.2, x2, y2 + (line - 1)*0.2)
        else:
            # diagonal
            super(FPDF_HTML, self).line(x1, y1, x2, y2)

        if color is not None:
            self.restore_draw_color()

    def dashed_line(self, x1, y1, x2, y2, dash_length=1, space_length=1, color=None, weight=1):
        if color is not None:
            self.set_draw_color(*color)

        if x1 == x2:
            # vertical
            for line in range(1, weight+1, 1):
                super(FPDF_HTML, self).dashed_line(x1 + (line - 1)*0.2, y1, x2 + (line - 1)*0.2, y2,
                                                   dash_length, space_length)
        elif y1 == y2:
            # horizontal
            for line in range(1, weight+1, 1):
                super(FPDF_HTML, self).dashed_line(x1, y1 + (line - 1)*0.2, x2, y2 + (line - 1)*0.2,
                                                   dash_length, space_length)
        else:
            # diagonal
            super(FPDF_HTML, self).dashed_line(x1, y1, x2, y2, dash_length, space_length)

        if color is not None:
            self.restore_draw_color()

        super(FPDF_HTML, self).dashed_line(x1, y1, x2, y2, dash_length, space_length)


class PDFMixin(object):
    FORMAT_A4 = 'A4'
    FORMATS = {
        FORMAT_A4: {
            'width': 210,
            'height': 297
        },
    }
    ORIENTATION_PORTRAIT = 'P'
    ORIENTATION_LANDSCAPE = 'L'
    ORIENTATIONS = (
        (ORIENTATION_PORTRAIT, _(u'Portrait')),
        (ORIENTATION_LANDSCAPE, _(u'Landscape'))
    )

    fpdf_class = FPDF_HTML
    filename = 'document.pdf'
    font = 'Arial'
    format = FORMAT_A4
    orientation = ORIENTATION_PORTRAIT
    unit = 'mm'
    margin_left = 10
    margin_right = 10
    margin_top = 10
    margin_bottom = 10
    override_header = True
    override_footer = True

    def render(self, **kwargs):
        # Go through keyword arguments and save their values to instance
        for key, value in six.iteritems(kwargs):
            setattr(self, key, value)

        self.init_sizes()
        self.init_pdf()
        self.write_content()

        self.response = HttpResponse(
            content=self.pdf.output(dest='S'),
            content_type='application/octet-stream'
        )
#        self.response['Content-Type'] = 'application/octet-stream; charset=UTF-8'
        self.response['Content-Disposition'] =\
            'attachment;filename="%(filename)s"' % {
                'filename': self.filename
            }
        return self.response

    def init_sizes(self):
        # page sizes
        self.page_width = self.FORMATS[self.format]['width']
        self.page_height = self.FORMATS[self.format]['height']

        if self.orientation == 'L':
            self.page_width, self.page_height = self.page_height, self.page_width

        # content sizes
        self.content_width = self.page_width - self.margin_left - self.margin_right
        self.content_height = self.page_height - self.margin_top - self.margin_bottom

    def get_pdf_instance(self):
        format_size = dict(self.FORMATS).get(self.format, None)
        format = self.format if format_size is None else (format_size['width'], format_size['height'])
        return self.fpdf_class(self.orientation, self.unit, format)

    def init_pdf(self, **kwargs):
        self.pdf = self.get_pdf_instance()

        if self.override_header:
            self.pdf.header = self.header

        if self.override_footer:
            self.pdf.footer = self.footer

        self.pdf.set_font(self.font, 'B')
        self.pdf.set_margins(self.margin_left, self.margin_top, self.margin_right)
        self.pdf.set_auto_page_break(True, margin=self.margin_bottom)
        self.pdf.add_page()
        self.pdf.alias_nb_pages()

        # Go through keyword arguments and save their values to instance
        for arg in kwargs:
            setattr(self.pdf, arg, kwargs.get(arg))

    def write_content(self):
        pass

    def header(self, *args, **kwargs):
        pass

    def footer(self, *args, **kwargs):
        pass


class PDFTablesMixin(PDFMixin):
    tables = []
    default_table_attrs = {
        'line_weight': {
            'horizontal': 1,
            'vertical': 1
        },
        'line_style': {
            'horizontal': 'solid',
            'vertical': 'solid'
        },
        'line_color': {
            'horizontal': colors.BLACK,
            'vertical': colors.BLACK
        },
        'widths': [1],
        'header': {
            'row_height': 10,
            'align': ['L'],
            'font_style': ['B'],
            'font_color': [colors.BLACK],
            'font_size': [12],
            'fill_color': [colors.SILVER],
            'max_chars': [None]
        },
        'body': {
            'row_height': 5,
            'align': ['L'],
            'font_style': [''],
            'font_color': [colors.BLACK],
            'font_size': [10],
            'fill_color': [None],
            'max_chars': [None]
        }
    }

    def write_before_tables(self):
        pass

    def write_after_tables(self):
        pass

    def write_before_table(self, index):
        pass

    def write_after_table(self, index):
        pass

    def check_page_break(self, y):
        if y > self.page_height - self.margin_bottom - self.table_attrs['body']['row_height']:
            self.pdf.add_page(self.orientation)
            self.pdf.set_y(self.pdf.t_margin)
            return True
        return False

    def write_table_row(self, columns, is_header=False):
        # check overflow
        self.check_page_break(self.pdf.get_y())

        x = self.pdf.l_margin
        y_init = self.pdf.get_y()
        y_max = None

        for index, text in enumerate(columns):
            column_width = self.get_column_attribute('width', index)
            column_align = self.get_column_attribute('align', index, is_header)
            column_font_color = self.get_column_attribute('font_color', index, is_header)
            column_font_style = self.get_column_attribute('font_style', index, is_header)
            column_fill_color = self.get_column_attribute('fill_color', index, is_header)
            fill = column_fill_color is not None
            if fill:
                self.pdf.set_fill_color(*column_fill_color)

            self.pdf.set_text_color(*column_font_color)
            self.pdf.set_font(self.font, column_font_style)
            self.pdf.multi_cell(
                w=column_width,
                h=self.table_attrs['header' if is_header else 'body']['row_height'],
                align=column_align,
                txt=text,
                border=False,
                fill=fill
            )

            self.pdf.restore_text_color()
            if fill:
                self.pdf.restore_fill_color()

            y = self.pdf.get_y()
            x += column_width

            if y_max is None or y > y_max:
                y_max = y
            self.pdf.set_xy(x, y_init)

        # vertical lines
        self.draw_vertical_lines(y_init, y_max)

        # check overflow
        if self.check_page_break(y_max):
            y_max = self.pdf.get_y()

        return y_max

    def write_table_header(self, header):
        # color and style
        color = self.table_attrs['line_color']['horizontal']
        style = self.table_attrs['line_style']['horizontal']
        weight = self.table_attrs['line_weight']['horizontal']

        if color:
            # line above header
            self.pdf.horizontal_line(self.pdf.l_margin, self.pdf.get_y(), self.content_width,
                                     weight=weight, color=color, style=style)

        # header columns
        y_pos = self.write_table_row(header, is_header=True)

        if color:
            # line below header
            self.pdf.horizontal_line(self.pdf.l_margin, y_pos, self.content_width,
                                     weight=weight, color=color, style=style)
        return y_pos

    def write_table_body(self, body):
        y_pos = self.pdf.get_y()
        for row in body:
            y_pos = self.write_table_row(row)
            self.pdf.set_xy(self.pdf.l_margin, y_pos)

            # color and style
            color = self.table_attrs['line_color']['horizontal']
            style = self.table_attrs['line_style']['horizontal']
            weight = self.table_attrs['line_weight']['horizontal']

            if color:
                # line after each row
                self.pdf.horizontal_line(self.pdf.l_margin, y_pos, self.content_width,
                                         weight=weight, color=color, style=style)
        return y_pos

    def write_table(self, table):
        # header
        header = table.get('header', None)

        if header:
            y_pos = self.write_table_header(header)
            self.pdf.set_xy(self.pdf.l_margin, y_pos)

        # body
        self.write_table_body(table['body'])

    def draw_vertical_lines(self, y_top, y_bottom):
        x = self.pdf.l_margin
        for index in range(0, self.number_of_columns+1):
            # color and style
            color = self.table_attrs['line_color']['vertical']
            style = self.table_attrs['line_style']['vertical']
            weight = self.table_attrs['line_weight']['vertical']

            if color:
                # vertical line
                self.pdf.line(x, y_top, x, y_bottom, weight=weight, color=color, style=style)
            column_width = self.get_column_attribute('width', index)
            x += column_width

    def write_content(self):
        self.validate_tables()

        self.write_before_tables()

        self.pdf.set_auto_page_break(False)
        for index, table in enumerate(self.tables):
            self.configure(table)
            self.write_before_table(index)
            self.write_table(table)
            self.write_after_table(index)
        self.pdf.set_auto_page_break(True, margin=self.margin_bottom)

        self.write_after_tables()

    def validate_tables(self):
        for table in self.tables:
            table_attrs = copy(self.default_table_attrs)
            default_header_attrs = copy(table_attrs['header'])
            default_body_attrs = copy(table_attrs['body'])
            default_line_color = copy(table_attrs['line_color'])
            default_line_style = copy(table_attrs['line_style'])
            default_line_weight = copy(table_attrs['line_weight'])

            table_attrs.update(table.get('attrs', {}))
            default_header_attrs.update(table_attrs['header'])
            default_body_attrs.update(table_attrs['body'])
            default_line_color.update(table_attrs['line_color'])
            default_line_style.update(table_attrs['line_style'])
            default_line_weight.update(table_attrs['line_weight'])

            table_attrs['header'].update(default_header_attrs)
            table_attrs['body'].update(default_body_attrs)
            table_attrs['line_color'].update(default_line_color)
            table_attrs['line_style'].update(default_line_style)
            table_attrs['line_weight'].update(default_line_weight)
            table['attrs'] = table_attrs

            if len(table['attrs'].get('widths')) <= 0:
                raise ValueError(_("Invalid value of 'widths'."))

            #TODO: more validation checks

    def configure(self, table):
        self.table_attrs = table['attrs']
        attrs = table['attrs']
        header = table.get('header', None)
        body = table['body']

        # calculate number of columns
        self.number_of_columns = 1
        if header:
            self.number_of_columns = len(header)
        else:
            try:
                self.number_of_columns = len(body[0])
            except IndexError:
                pass

        # calculate column widths
        widths = attrs.get('widths', [1])
        total_widths = sum((widths * (self.number_of_columns / len(widths) + 1))[:self.number_of_columns])
        self.column_widths = [float(column_width) * self.content_width/total_widths for column_width in widths]

    def get_column_attribute(self, attribute, index, is_header=False):
        if attribute == 'width':
            width_index = int(index % len(self.column_widths))
            return self.column_widths[width_index]

        attribute_values = self.table_attrs['header' if is_header else 'body'][attribute]
        attribute_index = int(index % len(attribute_values))
        return attribute_values[attribute_index]
