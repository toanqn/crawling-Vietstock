__author__ = 'toanqn'

import scrapy, re
from stock.items import StockItem

class VietStock(scrapy.Spider):
    name = 'vietstock1'
    allowed_domains = ['finance.vietstock.vn']
    start_urls = [
        "http://finance.vietstock.vn/doanh-nghiep-a-z/"
    ]
    base_url = 'http://finance.vietstock.vn/Controls/Report/Data/GetReport.ashx?rptType=BCTT&scode={}&bizType=1&rptUnit=1000000&rptTermTypeID=1&page={}'

    def parse(self, response):
        for selector in response.xpath("//b"):
            macp = selector.xpath('.//text()').extract_first('').strip()
            for i in range(1, 5):
                url = self.base_url.format(macp, i)
                # yield scrapy.Request(url, callback=self.parse_taichinh)

        print(response.xpath("//b//text()").extract_first())
        next_page = response.xpath("//td[span]/following-sibling::td")
        if next_page:
            next_link = next_page.xpath('./a/@href').extract_first('')
            page = re.match(r".*'(.*)','(.*)'\)", next_link)
            print(next_link)
            print(page.group(2))
            frmdata = {}
            frmdata['__EVENTARGUMENT'] = page.group(2)
            frmdata['__EVENTTARGET'] = page.group(1)
            frmdata['__VIEWSTATEFIELDCOUNT'] = response.xpath("//input[@id='__VIEWSTATEFIELDCOUNT']/@value").extract_first('').strip()
            frmdata['__EVENTVALIDATION'] = response.xpath("//input[@id='__EVENTVALIDATION']/@value").extract_first('').strip()
            frmdata['__VIEWSTATE'] = response.xpath("//input[@id='__VIEWSTATE']/@value").extract_first('').strip()

            frmdata['ctl00$cphCenter$IndDropDownList1$txtChooseInd'] = '[Tất cả]'
            frmdata['ctl00$cphCenter$IndDropDownList1$hdChooseIndId'] = '1'
            frmdata['ctl00$cphCenter$cboCatID'] = '0'
            frmdata['ctl00$cphCenter$cboCompanyTypeForSearch'] = '-1'
            frmdata['ctl00$cphCenter$txtKeyWord'] = ''

            for i in range(1, 255):
                frmdata['__VIEWSTATE{}'.format(i)] = response.xpath("//input[@id='__VIEWSTATE{}']/@value".format(i)).extract_first('').strip()
            # print(frmdata)
            yield scrapy.FormRequest.from_response(
                response,
                formdata=frmdata,
                callback=self.parse_page2,
                dont_filter=True
            )

    def parse_taichinh(self, response):
        print(11111)
        item = StockItem()
        if response.body:
            re_mack = re.match(r'.*&scode=(.*)&bizType.*', response.url)
            item['mack'] = re_mack.group(1)
            i = 1
            for sel in response.xpath("//tr[@class='BR_rowHeader']/td[position() > 1]"):
                item['date'] = sel.xpath('./text()').extract_first('').strip()

                item['dthuthuanve_bh_va_ccdv'] = response.xpath(
                    "//tr[@id='2216']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['giavon_bh'] = response.xpath("//tr[@id='2207']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['loinhuangopve_bh_va_ccdv'] = response.xpath(
                    "//tr[@id='2217']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['dthuhoatdong_tc'] = response.xpath("//tr[@id='2221']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['chiphi_tc'] = response.xpath("//tr[@id='2222']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['chiphi_bh'] = response.xpath("//tr[@id='2227']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['chiphi_qldn'] = response.xpath("//tr[@id='2224']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['loinhuanthuanve_hdkd'] = response.xpath("//tr[@id='2208']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['loinhuankhac'] = response.xpath("//tr[@id='2209']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['phanloinhuantucty_lkkd'] = response.xpath(
                    "//tr[@id='2210']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['tongloinhuanketoantrcthue'] = response.xpath(
                    "//tr[@id='2211']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['loinhuansauthue_tndn'] = response.xpath("//tr[@id='2212']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['loinhuansauthue_cuacongdongctyme'] = response.xpath(
                    "//tr[@id='2214']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['lai_cb_tren_cp'] = response.xpath("//tr[@id='2215']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()

                item['ts_nganhan'] = response.xpath("//tr[@id='3000']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['tienvacackhoan_td_tien'] = response.xpath(
                    "//tr[@id='3003']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['cackhoandautu_tcnh'] = response.xpath("//tr[@id='3004']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['cackhoanphaithunganhan'] = response.xpath(
                    "//tr[@id='3005']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['hangtonkho'] = response.xpath("//tr[@id='3006']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['taisannganhankhac'] = response.xpath("//tr[@id='3007']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['taisandaihan'] = response.xpath("//tr[@id='3001']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['taisancodinh'] = response.xpath("//tr[@id='3009']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['bds_dautu'] = response.xpath("//tr[@id='3010']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['cackhoandautu_tcdh'] = response.xpath("//tr[@id='3011']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['tongcongtaisan'] = response.xpath("//tr[@id='2996']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['nophaitra'] = response.xpath("//tr[@id='2997']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['nonganhan'] = response.xpath("//tr[@id='3014']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['nodaihan'] = response.xpath("//tr[@id='3017']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['vochusohuu'] = response.xpath("//tr[@id='2998']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['vondautucua_csh'] = response.xpath("//tr[@id='3063']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['thangduvon_cp'] = response.xpath("//tr[@id='3064']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()
                item['loinhuansauthue_chuapp'] = response.xpath(
                    "//tr[@id='3072']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['loiichcuacongdongthieuso'] = response.xpath(
                    "//tr[@id='3002']/td[{}]/text()".format(i + 2)).extract_first('').strip()
                item['tongcongnguonvon'] = response.xpath("//tr[@id='2999']/td[{}]/text()".format(i + 2)).extract_first(
                    '').strip()

                item['eps'] = response.xpath("//tr[@id='53']/td[{}]/text()".format(i + 3)).extract_first('').strip()
                item['bvps'] = response.xpath("//tr[@id='54']/td[{}]/text()".format(i + 3)).extract_first('').strip()
                item['p_e'] = response.xpath("//tr[@id='55']/td[{}]/text()".format(i + 3)).extract_first('').strip()
                item['p_b'] = response.xpath("//tr[@id='57']/td[{}]/text()".format(i + 3)).extract_first('').strip()
                item['tisuatloinhuangopbien'] = response.xpath("//tr[@id='41']/td[{}]/text()".format(i + 3)).extract_first(
                    '').strip()
                item['tisuatsinhloitrendoanhthuthuan'] = response.xpath(
                    "//tr[@id='44']/td[{}]/text()".format(i + 3)).extract_first('').strip()
                item['roea'] = response.xpath("//tr[@id='45']/td[{}]/text()".format(i + 3)).extract_first('').strip()
                item['roaa'] = response.xpath("//tr[@id='47']/td[{}]/text()".format(i + 3)).extract_first('').strip()
                item['tisothanhtoanhienhanh'] = response.xpath("//tr[@id='4']/td[{}]/text()".format(i + 3)).extract_first(
                    '').strip()
                item['khanangthanhtoanvaylai'] = response.xpath("//tr[@id='5']/td[{}]/text()".format(i + 3)).extract_first(
                    '').strip()
                item['tisonotrentrongtaisan'] = response.xpath("//tr[@id='8']/td[{}]/text()".format(i + 3)).extract_first(
                    '').strip()
                item['tisonotrenvonchusohuu'] = response.xpath("//tr[@id='11']/td[{}]/text()".format(i + 3)).extract_first(
                    '').strip()

                yield item