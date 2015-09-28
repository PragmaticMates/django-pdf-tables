from pdf_tables import colors
from pdf_tables.views import PDFTableView


class ExamplePDFView(PDFTableView):
    def dispatch(self, request, *args, **kwargs):
        self.build_tables()
        return super(ExamplePDFView, self).dispatch(request, *args, **kwargs)

    def write_after_table(self, index):
        if index == 4:
            color = self.table_attrs['border_color']['vertical']
            style = self.table_attrs['border_style']['vertical']
            width = self.table_attrs['border_width']['vertical']
            if color:
                self.pdf.horizontal_line(self.pdf.l_margin, self.pdf.get_y(), self.content_width,
                                         width=width, color=color, style=style)
        self.pdf.set_y(self.pdf.get_y()+10)

    def build_tables(self):
        self.tables = []
        self.tables.append({
            'attrs': {
                'border_color': {
                    'horizontal': colors.RED,
                    'vertical': colors.BLACK
                },
                'border_width': {
                    'horizontal': 3,
                    'vertical': 1
                },
                'widths': [10, 15, 20, 25, 30],
                'header': {
                    'line_height': [10],
                    'fill_color': [colors.WHITE, colors.SILVER, colors.GRAY, colors.DARK_GRAY, colors.BLACK],
                    'font_style': ['B', ''],
                    'font_color': [colors.BLACK, colors.BLACK, colors.BLACK, colors.WHITE, colors.WHITE]
                },
                'body': {
                    'line_height': [10],
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
                'border_width': {
                    'horizontal': 0,
                    'vertical': 0
                },
                'header': {
                    'line_height': [20]
                },
                'body': {
                    'line_height': [20],
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
                'border_width': {
                    'horizontal': 2,
                    'vertical': 2
                },
                'border_color': {
                    'horizontal': colors.WHITE,
                    'vertical': colors.WHITE
                },
                'header': {
                    'align': ['C'],
                    'line_height': [7],
                    'font_color': [colors.WHITE, colors.WHITE, colors.WHITE, colors.BLACK],
                    'fill_color': [colors.GREEN, colors.ORANGE, colors.RED, colors.YELLOW],
                },
                'body': {
                    'align': ['C'],
                    'line_height': [10],
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
                'border_color': {
                    'horizontal': colors.BLACK,
                    'vertical': None
                },
                'header': {
                    'align': ['C'],
                    'line_height': [7],
                    'fill_color': [colors.GRAY],
                    'font_color': [colors.WHITE],
                },
                'body': {
                    'align': ['C'],
                    'line_height': [7],
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
                'border_color': {
                    'horizontal': colors.WHITE,
                    'vertical': colors.BLACK
                },
                'header': {
                    'align': ['C'],
                    'line_height': [7],
                    'fill_color': [colors.GRAY],
                    'font_color': [colors.WHITE],
                },
                'body': {
                    'align': ['C'],
                    'line_height': [7],
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
                'border_style': {
                    'horizontal': 'solid',
                    'vertical': 'dashed'
                },
                'border_color': {
                    'horizontal': colors.BLACK,
                    'vertical': colors.BLACK
                },
                'header': {
                    'align': ['C'],
                    'line_height': [7],
                    'fill_color': [colors.GRAY],
                    'font_color': [colors.WHITE],
                },
                'body': {
                    'align': ['C'],
                    'line_height': [7],
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
                'border_style': {
                    'horizontal': 'dashed',
                    'vertical': 'solid'
                },
                'border_color': {
                    'horizontal': colors.BLACK,
                    'vertical': colors.SILVER
                },
                'border_width': {
                    'horizontal': 3,
                    'vertical': 1
                },
                'header': {
                    'align': ['C'],
                    'line_height': [7],
                    'fill_color': [colors.GRAY],
                    'font_color': [colors.WHITE],
                },
                'body': {
                    'align': ['C'],
                    'line_height': [7],
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
