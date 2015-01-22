from pdf_tables import colors
from pdf_tables.views import PDFTableView


class ExamplePDFView(PDFTableView):
    def dispatch(self, request, *args, **kwargs):
        self.build_tables()

        # add unicode font
        #from django.conf import settings
        #Arial_ttf = path.normpath(path.join(settings.SITE_ROOT, 'source/%s/static/fonts/arial/%s' % (settings.SITE_NAME, 'arial.ttf')))
        #ArialBold_ttf = path.normpath(path.join(settings.SITE_ROOT, 'source/%s/static/fonts/arial/%s' % (settings.SITE_NAME, 'arialbd.ttf')))
        #self.pdf.add_font('Arial', '', Arial_ttf, uni=True)
        #self.pdf.add_font('Arial', 'B', ArialBold_ttf, uni=True)
        #self.pdf.set_font(self.font, 'B')

        return self.render()

    def write_after_table(self, index):
        if index == 4:
            color = self.table_attrs['line_color']['vertical']
            style = self.table_attrs['line_style']['vertical']
            weight = self.table_attrs['line_weight']['vertical']
            if color:
                self.pdf.horizontal_line(self.pdf.l_margin, self.pdf.get_y(), self.content_width,
                                         weight=weight, color=color, style=style)
        self.pdf.set_y(self.pdf.get_y()+10)

    def build_tables(self):
        self.tables.append({
            'attrs': {
                'line_color': {
                    'horizontal': colors.RED,
                    'vertical': colors.BLACK
                },
                'line_weight': {
                    'horizontal': 3,
                    'vertical': 1
                },
                'widths': [10, 15, 20, 25, 30],
                'header': {
                    'height': [10],
                    'fill_color': [colors.WHITE, colors.SILVER, colors.GRAY, colors.DARK_GRAY, colors.BLACK],
                    'font_style': ['B', ''],
                    'font_color': [colors.BLACK, colors.BLACK, colors.BLACK, colors.WHITE, colors.WHITE]
                },
                'body': {
                    'height': [10],
                    'font_style': ['']
                }
            },
            'header': ['A letter', 'B letter', 'C letter', 'D letter', 'E letter'],
            'body': [
                ['1A', '1B', '1C', '1D', '1E'],
                ['2A', '2B', '2C', '2D', '2E'],
                ['3A', '3B', '3C', '3D', '3E'],
                ['4A', '4B', '4C', '4D', '4E'],
                ['5A', '5B', '5C', '5D', '5E']
            ]
        })
        self.tables.append({
            'attrs': {
                'line_weight': {
                    'horizontal': 0,
                    'vertical': 0
                },
                'header': {
                    'height': [20]
                },
                'body': {
                    'height': [20],
                    'align': ['L', 'C', 'R']
                }
            },
            'body': [
                ['left top', 'center top', 'right top'],
                ['left middle', 'center middle', 'right middle'],
                ['left bottom', 'center bottom', 'right bottom']
            ]
        })
        self.tables.append({
            'attrs': {
                'line_weight': {
                    'horizontal': 2,
                    'vertical': 2
                },
                'line_color': {
                    'horizontal': colors.WHITE,
                    'vertical': colors.WHITE
                },
                'header': {
                    'align': ['C'],
                    'height': [7],
                    'font_color': [colors.WHITE, colors.WHITE, colors.WHITE, colors.BLACK],
                    'fill_color': [colors.GREEN, colors.ORANGE, colors.RED, colors.YELLOW],
                },
                'body': {
                    'align': ['C'],
                    'height': [10],
                    'font_color': [colors.GREEN, colors.ORANGE, colors.RED, colors.YELLOW],
                }
            },
            'header': ['apple', 'orange', 'strawberry', 'banana'],
            'body': [
                ['01', '02', '03', '04'],
                ['05', '06', '07', '08'],
                ['09', '10', '11', '12'],
                ['13', '14', '15', '16']
            ]
        })
        self.tables.append({
            'attrs': {
                'line_color': {
                    'horizontal': colors.BLACK,
                    'vertical': None
                },
                'header': {
                    'align': ['C'],
                    'height': [7],
                    'fill_color': [colors.GRAY],
                    'font_color': [colors.WHITE],
                },
                'body': {
                    'align': ['C'],
                    'height': [7],
                    'font_color': [colors.GRAY],
                }
            },
            'header': ['A', 'B', 'C', 'D', 'E'],
            'body': [
                ['01', '02', '03', '04', '05'],
                ['06', '07', '08', '09', '10'],
                ['11', '12', '13', '14', '15'],
                ['16', '17', '18', '19', '20'],
                ['21', '22', '23', '24', '25']
            ]
        })
        self.tables.append({
            'attrs': {
                'line_color': {
                    'horizontal': colors.WHITE,
                    'vertical': colors.BLACK
                },
                'header': {
                    'align': ['C'],
                    'height': [7],
                    'fill_color': [colors.GRAY],
                    'font_color': [colors.WHITE],
                },
                'body': {
                    'align': ['C'],
                    'height': [7],
                    'font_color': [colors.GRAY],
                }
            },
            'header': ['A', 'B', 'C', 'D', 'E'],
            'body': [
                ['01', '02', '03', '04', '05'],
                ['06', '07', '08', '09', '10'],
                ['11', '12', '13', '14', '15'],
                ['16', '17', '18', '19', '20'],
                ['21', '22', '23', '24', '25']
            ]
        })
        self.tables.append({
            'attrs': {
                'line_style': {
                    'horizontal': 'solid',
                    'vertical': 'dashed'
                },
                'line_color': {
                    'horizontal': colors.BLACK,
                    'vertical': colors.BLACK
                },
                'header': {
                    'align': ['C'],
                    'height': [7],
                    'fill_color': [colors.GRAY],
                    'font_color': [colors.WHITE],
                },
                'body': {
                    'align': ['C'],
                    'height': [7],
                    'font_color': [colors.GRAY],
                }
            },
            'header': ['A', 'B', 'C', 'D', 'E'],
            'body': [
                ['01', '02', '03', '04', '05'],
                ['06', '07', '08', '09', '10'],
                ['11', '12', '13', '14', '15'],
                ['16', '17', '18', '19', '20'],
                ['21', '22', '23', '24', '25']
            ]
        })
        self.tables.append({
            'attrs': {
                'line_style': {
                    'horizontal': 'dashed',
                    'vertical': 'solid'
                },
                'line_color': {
                    'horizontal': colors.BLACK,
                    'vertical': colors.SILVER
                },
                'line_weight': {
                    'horizontal': 3,
                    'vertical': 1
                },
                'header': {
                    'align': ['C'],
                    'height': [7],
                    'fill_color': [colors.GRAY],
                    'font_color': [colors.WHITE],
                },
                'body': {
                    'align': ['C'],
                    'height': [7],
                    'font_color': [colors.GRAY],
                }
            },
            'header': ['A', 'B', 'C', 'D', 'E'],
            'body': [
                ['01', '02', '03', '04', '05'],
                ['06', '07', '08', '09', '10'],
                ['11', '12', '13', '14', '15'],
                ['16', '17', '18', '19', '20'],
                ['21', '22', '23', '24', '25']
            ]
        })
