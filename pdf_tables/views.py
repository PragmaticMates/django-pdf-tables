from django.views.generic import View

from mixins import PDFMixin, PDFTablesMixin


class PDFView(PDFMixin, View):
    DEBUG = False

    def dispatch(self, request, *args, **kwargs):
        return self.render()

    #def get_pdf_instance(self):
    #        def get_content_width(self):
    #            return self.w - self.l_margin - self.r_margin
    #
    #        def get_content_height(self):
    #            return self.h - self.t_margin - self.b_margin
    #
    #        def get_half_content_width(self):
    #            return float(self.get_content_width()) / 2
    #
    #        def get_half_page_width(self):
    #            return float(self.w) / 2
    #
    #        def set_font_title(self):
    #            self.set_font(self.font, 'B', self.font_size_title)
    #
    #        def set_font_subtitle(self):
    #            self.set_font(self.font, '', self.font_size_subtitle)
    #
    #        def set_font_normal(self):
    #            self.set_font(self.font, '', self.font_size_normal)
    #
    #        def set_font_small(self):
    #            self.set_font(self.font, '', self.font_size_small)
    #
    #        def set_font_tiny(self):
    #            self.set_font(self.font, '', self.font_size_tiny)
    #
    #        def set_font_bold(self):
    #            self.set_font(self.font, 'B', self.font_size_normal)
    #
    #        def set_font_bold_small(self):
    #            self.set_font(self.font, 'B', self.font_size_small)
    #
    #        def set_font_bold_subtitle(self):
    #            self.set_font(self.font, 'B', self.font_size_subtitle)
    #
    #        def set_font_bold_tiny(self):
    #            self.set_font(self.font, 'B', self.font_size_tiny)
    #
    #        def header(self):
    #            if self.page_no() == 1:
    #
    #            else:
    #
    #            # LINE
    #            y = self.TOP_LINE_Y
    #            self.line(self.l_margin, y, self.w - self.r_margin, y)
    #
    #        def footer(self):
    #            if self.page_no() == 1:
    #                pager_width = 20
    #                date_and_city_width = self.get_content_width() - pager_width
    #
    #                date_and_city = ugettext('%(date)s in %(city)s') % {
    #                    'date': datetime.strftime(self.protocol.date.astimezone(get_default_timezone()), settings.DATE_FORMAT),
    #                    'city': self.protocol.city
    #                }
    #                self.set_y(self.h - 14 - self.cell_height_normal)
    #                mark_y = self.get_y()
    #                self.set_font_normal()
    #                self.multi_cell(w=date_and_city_width, h=self.cell_height_normal, txt=date_and_city, border=self.DEBUG, align='L', fill=False)
    #                self.set_xy(self.l_margin + date_and_city_width, mark_y)
    #                self.multi_cell(w=pager_width, h=self.cell_height_normal, txt=('%s/{nb}' % self.page_no()).strip(), border=self.DEBUG, align='R', fill=False)
    #            else:
    #
    #                self.set_y(self.h - 18 + 1)
    #                self.set_font_bold_tiny()
    #                self.multi_cell(w=30, h=4, txt=ugettext(u'Legend') + ':', border=self.DEBUG, align='L', fill=False)
    #                mark_y = self.get_y()
    #                self.set_x(self.l_margin)
    #                for legend in legends:
    #                    self.set_x(self.l_margin)
    #                    for l_index, l in enumerate(legend):
    #                        width = l['width_a'] + l['width_d']
    #                        x = self.get_x()
    #                        #self.set_font_bold_tiny()
    #                        #self.multi_cell(w=l['width_a'], h=4, txt=l['abbreviation'], border=self.DEBUG, align='L', fill=False)
    #                        #self.set_xy(x + l['width_a'], mark_y)
    #                        #self.set_font_tiny()
    #                        #self.multi_cell(w=l['width_d'], h=4, txt='- %s' % l['description'], border=self.DEBUG, align='L', fill=False)
    #                        self.set_font_tiny()
    #                        self.multi_cell(w=width, h=4, txt='%s - %s' % (l['abbreviation'], l['description']), border=self.DEBUG, align='L', fill=False)
    #                        if l_index == len(legend) - 1:
    #                            mark_y = self.get_y()
    #                        self.set_xy(x + width, mark_y)
    #
    #                # LINE
    #                y = self.h - 18
    #                self.line(self.l_margin, y, self.w - self.r_margin, y)
    #
    #                # PAGER
    #                pager_width = 20
    #                self.set_xy(self.w - pager_width - self.r_margin, self.h - 14)
    #                self.set_font_normal()
    #                self.multi_cell(w=pager_width, h=self.cell_height_normal, txt=('%s/{nb}' % self.page_no()).strip(), border=self.DEBUG, align='R', fill=False)
    #
    #    return ProtocolFPDF(protocol=self.protocol, **self.options)
    #
    #def write_first_page(self):
    #    # TITLE #
    #    # ---------------------------------------------------------------- #
    #    self.pdf.set_font_title()
    #    title = _('%(protocol_type)s #%(code)s') % {
    #        'protocol_type': self.get_title(),
    #        'code': self.protocol.code
    #    }
    #
    #    self.pdf.set_xy(self.margin_left, self.TOP_LINE_Y + 13)
    #    self.pdf.multi_cell(w=self.content_width, h=self.pdf.cell_height_title, txt=title, border=self.DEBUG, align='L', fill=False)
    #
    #    subtitle = self.get_subtitle()
    #    if subtitle:
    #        # SUBTITLE #
    #        # ---------------------------------------------------------------- #
    #        self.pdf.set_font_subtitle()
    #        self.pdf.set_xy(self.margin_left, self.pdf.get_y())
    #        self.pdf.multi_cell(w=self.content_width, h=self.pdf.cell_height_subtitle, txt=subtitle, border=self.DEBUG, align='L', fill=False)
    #
    #    # SIDES #
    #    mark_y = self.pdf.get_y() + 18
    #    side_size = self.half_content_width - 9
    #
    #    # USER GIVER #
    #    # ---------------------------------------------------------------- #
    #    self.pdf.set_font_bold_subtitle()
    #    self.pdf.set_xy(self.margin_left, mark_y)
    #    self.pdf.multi_cell(w=side_size, h=self.pdf.cell_height_subtitle, txt=ugettext(u'Giver') + ':', border=self.DEBUG, align='L', fill=False)
    #
    #    # GIVER LOGO
    #    # GET LOGO FILEPATH
    #    filepath = self.get_giver().get('logo_path', None)
    #    if filepath and path.exists(filepath):
    #        from PIL import Image
    #        im = Image.open(filepath)
    #        i_width, i_height = im.size
    #        i_size_ratio = float(i_width) / i_height
    #
    #        # CALCULATE IMAGE SIZE
    #        l_height = self.LOGO_HEIGHT
    #        l_width = float(l_height) * i_size_ratio
    #
    #        # CHECK OVERFLOW
    #        if l_width > side_size:
    #            l_width = side_size
    #            l_height = float(l_width) / i_size_ratio
    #
    #        # CALCULATE POSITION
    #        x = self.margin_left
    #        y = self.pdf.get_y() + 1
    #
    #        # WRITE IMAGE
    #        self.pdf.image(filepath, x=x, y=y, w=l_width, h=l_height, type='', link='')
    #
    #    self.pdf.set_y(self.pdf.get_y() + self.LOGO_HEIGHT + 2)
    #    self.pdf.set_font_bold()
    #    self.pdf.multi_cell(w=side_size, h=self.pdf.cell_height_normal, txt=self.get_giver()['company'], border=self.DEBUG, align='L', fill=False)
    #    self.pdf.set_font_normal()
    #    self.pdf.multi_cell(w=side_size, h=self.pdf.cell_height_normal, txt=self.get_giver()['street'], border=self.DEBUG, align='L', fill=False)
    #    self.pdf.multi_cell(w=side_size, h=self.pdf.cell_height_normal, txt=self.get_giver()['zip_city'], border=self.DEBUG, align='L', fill=False)
    #    self.pdf.multi_cell(w=side_size, h=self.pdf.cell_height_normal, txt=u'%s: %s' % (ugettext(u'ID'), self.get_giver()['company_id']), border=self.DEBUG, align='L', fill=False)
    #
    #    # DASHED LINE
    #    self.pdf.set_y(self.pdf.get_y() + 15)
    #    dashed_line_width = side_size
    #    self.pdf.dashed_line(self.pdf.l_margin, self.pdf.get_y(), self.pdf.l_margin + dashed_line_width, self.pdf.get_y(), dash_length=1, space_length=1)
    #    giver_name = self.protocol.user_giver.get_full_name() if self.protocol.user_giver else ''
    #    self.pdf.set_y(self.pdf.get_y() + 3)
    #    self.pdf.multi_cell(w=side_size, h=self.pdf.cell_height_normal, txt=giver_name, border=self.DEBUG, align='L', fill=False)
    #
    #    # USER TAKER #
    #    # ---------------------------------------------------------------- #
    #    mark_x = self.half_page_width + 9
    #    self.pdf.set_font_bold_subtitle()
    #    self.pdf.set_xy(mark_x, mark_y)
    #    self.pdf.multi_cell(w=side_size, h=self.pdf.cell_height_subtitle, txt=ugettext(u'Taker') + ':', border=self.DEBUG, align='L', fill=False)
    #
    #    # TAKER LOGO
    #    filepath = self.get_taker().get('logo_path', None)
    #    if filepath and path.exists(filepath):
    #        # GET IMAGE DIMENSIONS
    #        from PIL import Image
    #        im = Image.open(filepath)
    #        i_width, i_height = im.size
    #        i_size_ratio = float(i_width) / i_height
    #
    #        # CALCULATE IMAGE SIZE
    #        l_height = self.LOGO_HEIGHT
    #        l_width = float(l_height) * i_size_ratio
    #
    #        # CHECK OVERFLOW
    #        if l_width > side_size:
    #            l_width = side_size
    #            l_height = float(l_width) / i_size_ratio
    #
    #        # CALCULATE POSITION
    #        x = self.margin_left
    #        y = self.pdf.get_y() + 1
    #
    #        # WRITE IMAGE
    #        self.pdf.image(filepath, x=mark_x, y=y, w=l_width, h=l_height, type='', link='')
    #
    #    self.pdf.set_y(self.pdf.get_y() + 20)
    #    self.pdf.set_font_bold()
    #    self.pdf.set_x(mark_x)
    #    self.pdf.multi_cell(w=side_size, h=self.pdf.cell_height_normal, txt=self.get_taker()['company'] or '', border=self.DEBUG, align='L', fill=False)
    #    self.pdf.set_font_normal()
    #    self.pdf.set_x(mark_x)
    #    self.pdf.multi_cell(w=side_size, h=self.pdf.cell_height_normal, txt=self.get_taker()['street'] or '', border=self.DEBUG, align='L', fill=False)
    #    self.pdf.set_x(mark_x)
    #    self.pdf.multi_cell(w=side_size, h=self.pdf.cell_height_normal, txt=self.get_taker()['zip_city'] or '', border=self.DEBUG, align='L', fill=False)
    #    self.pdf.set_x(mark_x)
    #    self.pdf.multi_cell(w=side_size, h=self.pdf.cell_height_normal, txt=u'%s: %s' % (ugettext(u'ID'), self.get_taker()['company_id'] or ''), border=self.DEBUG, align='L', fill=False)
    #    # DASHED LINE
    #    self.pdf.set_y(self.pdf.get_y() + 15)
    #    dashed_line_width = side_size
    #    self.pdf.dashed_line(mark_x, self.pdf.get_y(), mark_x + dashed_line_width, self.pdf.get_y(), dash_length=1, space_length=1)
    #    taker_name = self.protocol.user_taker.get_full_name() if self.protocol.user_taker else ''
    #    self.pdf.set_xy(mark_x, self.pdf.get_y() + 3)
    #    self.pdf.multi_cell(w=side_size, h=self.pdf.cell_height_normal, txt=taker_name, border=self.DEBUG, align='L', fill=False)
    #
    #    # STATISTICS #
    #    # ---------------------------------------------------------------- #
    #    number_cell_width = 20
    #    label_width = self.content_width - number_cell_width
    #    self.pdf.set_font_bold_subtitle()
    #    self.pdf.set_xy(self.margin_left, self.page_height - 95)
    #    self.pdf.multi_cell(w=self.content_width, h=self.pdf.cell_height_subtitle, txt=ugettext(u'Statistics information') + ':', border=self.DEBUG, align='L', fill=False)
    #    self.pdf.set_y(self.pdf.get_y() + 8)
    #    self.pdf.set_font_normal()
    #
    #    mark_y = self.pdf.get_y()
    #    number = self.get_boxes_count()
    #    self.pdf.multi_cell(w=label_width, h=self.pdf.cell_height_normal, txt=ugettext(u'Number of boxes') + ':', border=self.DEBUG, align='L', fill=False)
    #    self.pdf.set_xy(self.margin_left + label_width, mark_y)
    #    self.pdf.multi_cell(w=number_cell_width, h=self.pdf.cell_height_normal, txt=str(number), border=self.DEBUG, align='R', fill=False)
    #    self.pdf.line(self.margin_left, self.pdf.get_y() + 1, self.page_width - self.margin_right, self.pdf.get_y() + 1, color='silver')
    #
    #    self.pdf.set_y(self.pdf.get_y() + 2)
    #    mark_y = self.pdf.get_y()
    #    number = self.get_queryset().count()
    #    self.pdf.multi_cell(w=label_width, h=self.pdf.cell_height_normal, txt=ugettext(u'Number of storage units') + ':', border=self.DEBUG, align='L', fill=False)
    #    self.pdf.set_xy(self.margin_left + label_width, mark_y)
    #    self.pdf.multi_cell(w=number_cell_width, h=self.pdf.cell_height_normal, txt=str(number), border=self.DEBUG, align='R', fill=False)
    #    self.pdf.line(self.margin_left, self.pdf.get_y() + 1, self.page_width - self.margin_right, self.pdf.get_y() + 1, color='silver')
    #
    #    self.pdf.set_y(self.pdf.get_y() + 2)
    #    mark_y = self.pdf.get_y()
    #    units_limit_mark = self.get_queryset().filter(document_type__ap_row__limit_mark='A')
    #    number = units_limit_mark.count()
    #    self.pdf.multi_cell(w=label_width, h=self.pdf.cell_height_normal, txt=ugettext(u'Number of storage units with limit mark A') + ':', border=self.DEBUG, align='L', fill=False)
    #    self.pdf.set_xy(self.margin_left + label_width, mark_y)
    #    self.pdf.multi_cell(w=number_cell_width, h=self.pdf.cell_height_normal, txt=str(number), border=self.DEBUG, align='R', fill=False)
    #    self.pdf.line(self.margin_left, self.pdf.get_y() + 1, self.page_width - self.margin_right, self.pdf.get_y() + 1, color='silver')
    #
    #    self.pdf.set_y(self.pdf.get_y() + 2)
    #    mark_y = self.pdf.get_y()
    #    units_no_limit_mark = self.get_queryset().exclude(document_type__ap_row__limit_mark='A')
    #    number = units_no_limit_mark.count()
    #    self.pdf.multi_cell(w=label_width, h=self.pdf.cell_height_normal, txt=ugettext(u'Number of storage units without limit mark A') + ':', border=self.DEBUG, align='L', fill=False)
    #    self.pdf.set_xy(self.margin_left + label_width, mark_y)
    #    self.pdf.multi_cell(w=number_cell_width, h=self.pdf.cell_height_normal, txt=str(number), border=self.DEBUG, align='R', fill=False)
    #
    #def write_pdf_content(self):
    #    self.write_first_page()
    #    self.write_tables()
    #
    #def write_tables(self):
    #    self.pdf.add_page(FPDFMixin.ORIENTATION_LANDSCAPE)
    #    self.pdf.set_font_small()
    #
    #    self.pdf.set_xy(self.margin_left, self.TOP_LINE_Y + 4)
    #
    #    print_header = True
    #
    #    # HELPER FUNCTION
    #    def row(columns):
    #        column_sizes = [10, 12, 30, 30, 17, 15, 63, 33, 30, 14, 8, 9]
    #        y_init = self.pdf.get_y()
    #        x = self.pdf.l_margin
    #        y_max = None
    #        for index, column in enumerate(columns):
    #            if column.get('bold', False):
    #                self.pdf.set_font_bold_small()
    #            else:
    #                self.pdf.set_font_small()
    #            column_width = column_sizes[index]
    #            self.pdf.multi_cell(w=column_width, h=column.get('height', self.pdf.cell_height_normal), txt=column['text'], border=self.DEBUG, align=column['align'], fill=column.get('fill', False))
    #            y = self.pdf.get_y()
    #            x += column_width
    #            if y_max is None or y > y_max:
    #                y_max = y
    #            self.pdf.set_xy(x, y_init)
    #        return y_max
    #
    #    def write_table_header():
    #        self.pdf.set_fill_color(202, 202, 202)
    #        # TABLE HEADER
    #        y_pos = row([
    #            {'text': '#', 'align': "L", 'bold': True, 'fill': True},
    #            {'text': pgettext("abbreviation", u'BOX'), 'align': "L", 'bold': True, 'fill': True},
    #            {'text': pgettext("abbreviation", u'BRNCH'), 'align': "L", 'bold': True, 'fill': True},
    #            {'text': pgettext("abbreviation", u'DEP'), 'align': "L", 'bold': True, 'fill': True},
    #            {'text': pgettext("abbreviation", u'RCVD'), 'align': "L", 'bold': True, 'fill': True},
    #            {'text': pgettext("abbreviation", u'SU'), 'align': "L", 'bold': True, 'fill': True},
    #            {'text': pgettext("abbreviation", u'DESCRIPTION'), 'align': "L", 'bold': True, 'fill': True},
    #            {'text': pgettext("abbreviation", u'DATE R.'), 'align': "L", 'bold': True, 'fill': True},
    #            {'text': pgettext("abbreviation", u'NUMBER R.'), 'align': "L", 'bold': True, 'fill': True},
    #            {'text': pgettext("abbreviation", u'AR'), 'align': "R", 'bold': True, 'fill': True},
    #            {'text': pgettext("abbreviation", u'LV'), 'align': "R", 'bold': True, 'fill': True},
    #            {'text': pgettext("abbreviation", u'DISP'), 'align': "R", 'bold': True, 'fill': True},
    #        ])
    #        return y_pos
    #
    #    # TABLE BODY
    #    for index, unit in enumerate(self.get_queryset()):
    #        y = self.pdf.get_y()
    #
    #        if print_header:
    #            # TABLE HEADER
    #            y = write_table_header()
    #            print_header = False
    #
    #        self.pdf.set_xy(self.pdf.l_margin, y)
    #        mark_y = y
    #        self.pdf.set_y(y + 1.5)
    #
    #        if isinstance(unit, Document):
    #            number_range = '%s%s' % (unit.number_prefix or '', unit.number)
    #            date_range = datetime.strftime(unit.date.astimezone(get_default_timezone()), settings.DATE_FORMAT) if unit.date is not None else ''
    #        else:
    #            try:
    #                number_range = ''
    #                count_ranges = unit.numberrange_set.all().count()
    #                for r_index, range in enumerate(unit.numberrange_set.all()):
    #                    number_range += '%s%s - %s%s' % (unit.number_prefix or '', range.number_from, unit.number_prefix or '', range.number_to)
    #                    if r_index != count_ranges - 1:
    #                        number_range += ', '
    #            except AttributeError:
    #                number_range = ''
    #
    #            try:
    #                try:
    #                    date_from = datetime.strftime(unit.date_from.astimezone(get_default_timezone()), settings.DATE_FORMAT) if unit.date_from is not None else ''
    #                except ValueError:
    #                    date_from = unicode(unit.date_from)
    #
    #                try:
    #                    date_to = datetime.strftime(unit.date_to.astimezone(get_default_timezone()), settings.DATE_FORMAT) if unit.date_to is not None else ''
    #                except ValueError:
    #                    date_to = unicode(unit.date_to)
    #
    #                date_range = u'%s - %s' % (date_from, date_to)
    #            except AttributeError:
    #                date_range = ''
    #
    #
    #        desc = unit.description
    #
    #        if self.DEBUG:
    #            desc = 'kde bolo tam bolo, tralala tralala ako sa mas? skusam skusam pisem zvasty, faktury, manualy, rezervy kolace, chladnicka a jedlo, superfaktury a zmluvy a neviem co este, skratka potrebujem naplnit tri riadky textu'
    #
    #        description = unicode(desc[:130] + (desc[130:] and u'...')) if desc else ''
    #
    #        y = row([
    #            {'text': '%d.' % (index + 1), 'align': "L", 'bold': True, 'height': self.pdf.cell_height_tiny},
    #            {'text': str(unit.box.code) if unit.box else u'-', 'align': "L", 'bold': False, 'height': self.pdf.cell_height_tiny},
    #            {'text': str(unit.department.branch), 'align': "L", 'bold': False, 'height': self.pdf.cell_height_tiny},
    #            {'text': str(unit.department), 'align': "L", 'bold': False, 'height': self.pdf.cell_height_tiny},
    #            {'text': datetime.strftime(unit.receive_date.astimezone(get_default_timezone()), settings.DATE_FORMAT), 'align': "L", 'bold': False, 'height': self.pdf.cell_height_tiny},
    #            {'text': str(unit.code), 'align': "L", 'bold': False, 'height': self.pdf.cell_height_tiny},
    #            #{'text': str(unit.description), 'align': "L", 'bold': False, 'height': self.pdf.cell_height_tiny},
    #            {'text': description, 'align': "L", 'bold': False, 'height': self.pdf.cell_height_tiny},
    #            {'text': date_range, 'align': "L", 'bold': False, 'height': self.pdf.cell_height_tiny},
    #            {'text': number_range, 'align': "L", 'bold': False, 'height': self.pdf.cell_height_tiny},
    #            {'text': str(unit.document_type.ap_row.code), 'align': "R", 'bold': False, 'height': self.pdf.cell_height_tiny},
    #            {'text': '%s%d' % (str(unit.document_type.ap_row.limit_mark or ''), unit.document_type.ap_row.limit_value), 'align': "R", 'bold': False, 'height': self.pdf.cell_height_tiny},
    #            {'text': str(unit.disposal_year), 'align': "R", 'bold': False, 'height': self.pdf.cell_height_tiny},
    #        ])
    #
    #        y += 1.5
    #        # bottom line
    #        self.pdf.line(self.pdf.l_margin, y, self.pdf.w - self.pdf.r_margin, y, color='silver')
    #        # left line
    #        self.pdf.line(self.pdf.l_margin, mark_y, self.pdf.l_margin, y, color='silver')
    #        # right line
    #        self.pdf.line(self.pdf.w - self.pdf.r_margin - 0.2, mark_y, self.pdf.w - self.pdf.r_margin - 0.2, y, color='silver')
    #
    #        self.pdf.set_y(y)
    #        #y = row([
    #        #    {'text': '999.', 'align': "L", 'bold': True},
    #        #    {'text': 'A10000', 'align': "L", 'bold': False},
    #        #    {'text': 'ZSR Generalne riaditelstvo', 'align': "L", 'bold': False},
    #        #    {'text': 'Financne oddelenie', 'align': "L", 'bold': False},
    #        #    {'text': '33.44.9999', 'align': "L", 'bold': False},
    #        #    {'text': 'Q1234567890', 'align': "L", 'bold': False},
    #        #    {'text': 'Lorem impsum dolor sit amet abrakadabra, faktury dosle, manualy, CD a ine zvasty', 'align': "L", 'bold': False},
    #        #    {'text': '33.44.9999 - 33.44.9999, 33.44.9999 - 33.44.9999', 'align': "L", 'bold': False},
    #        #    {'text': 'FAK1000 - FAK2000, FAK1000 - FAK2000, FAK1000 - FAK2000', 'align': "L", 'bold': False},
    #        #    {'text': 'GRP12.3', 'align': "R", 'bold': False},
    #        #    {'text': 'A70', 'align': "R", 'bold': False},
    #        #    {'text': '9999', 'align': "R", 'bold': False},
    #        #])
    #        #self.pdf.line(self.pdf.l_margin, y, self.pdf.w - self.pdf.r_margin, y, color='silver')
    #        #self.pdf.set_y(y)
    #        #y = row([
    #        #    {'text': '999.', 'align': "L", 'bold': True},
    #        #    {'text': 'A10000', 'align': "L", 'bold': False},
    #        #    {'text': 'ZSR Generalne riaditelstvo', 'align': "L", 'bold': False},
    #        #    {'text': 'Financne oddelenie', 'align': "L", 'bold': False},
    #        #    {'text': '33.44.9999', 'align': "L", 'bold': False},
    #        #    {'text': 'Z10000', 'align': "L", 'bold': False},
    #        #    {'text': 'Lorem impsum dolor sit amet abrakadabra, faktury dosle, manualy, CD a ine zvasty', 'align': "L", 'bold': False},
    #        #    {'text': '33.44.9999 - 33.44.9999, 33.44.9999 - 33.44.9999', 'align': "L", 'bold': False},
    #        #    {'text': 'FAK1000 - FAK2000, FAK1000 - FAK2000, FAK1000 - FAK2000', 'align': "L", 'bold': False},
    #        #    {'text': 'GRP12.3', 'align': "R", 'bold': False},
    #        #    {'text': 'A70', 'align': "R", 'bold': False},
    #        #    {'text': '9999', 'align': "R", 'bold': False},
    #        #])
    #
    #        self.pdf.set_y(y)
    #
    #        # ADD NEW PAGE IF OVERFLOW
    #        if self.pdf.get_y() > 180 and index < self.get_queryset().count() - 1:
    #            print_header = True
    #            self.pdf.add_page(FPDFMixin.ORIENTATION_LANDSCAPE)
    #            self.pdf.set_y(self.TOP_LINE_Y + 4)
    #
    #            #y += 1.5
    #            #self.pdf.line(self.pdf.l_margin, y, self.page_width - self.pdf.r_margin, y, 'grey')
    #            #y += 1
    #            #self.pdf.line(self.pdf.l_margin, y, self.page_width - self.pdf.r_margin, y, 'grey')


class PDFTableView(PDFTablesMixin, PDFView):
    pass
