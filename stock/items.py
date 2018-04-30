# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
#    ket qua kinh doanh
    mack = scrapy.Field()
    dthuthuanve_bh_va_ccdv = scrapy.Field()
    giavon_bh = scrapy.Field()
    loinhuangopve_bh_va_ccdv = scrapy.Field()
    dthuhoatdong_tc = scrapy.Field()
    chiphi_tc = scrapy.Field()
    chiphi_bh = scrapy.Field()
    chiphi_qldn = scrapy.Field()
    loinhuanthuanve_hdkd = scrapy.Field()
    loinhuankhac = scrapy.Field()
    phanloinhuantucty_lkkd = scrapy.Field()
    tongloinhuanketoantrcthue = scrapy.Field()
    loinhuansauthue_tndn = scrapy.Field()
    loinhuansauthue_cuacongdongctyme = scrapy.Field()
    lai_cb_tren_cp =scrapy.Field()

    doanhthuthuan_hdkd_bh = scrapy.Field()
    tongchitructiep_hdkd_bh = scrapy.Field()
    loinhuangop_hdkd_bh = scrapy.Field()
    loinhuanthuan_hdkd_bh = scrapy.Field()
    loinhuan_hdtc = scrapy.Field()
    loinhuan_hdkhac = scrapy.Field()
    tongloinhuanketoan = scrapy.Field()


#     can doi ke toan
    ts_nganhan = scrapy.Field()
    tienvacackhoan_td_tien = scrapy.Field()
    cackhoandautu_tcnh = scrapy.Field()
    cackhoanphaithunganhan = scrapy.Field()
    cackhoanphaithudaihan = scrapy.Field()
    hangtonkho = scrapy.Field()
    taisannganhankhac = scrapy.Field()
    taisandaihankhac = scrapy.Field()
    loithethuongmai = scrapy.Field()
    taisandaihan = scrapy.Field()
    taisancodinh = scrapy.Field()
    bds_dautu = scrapy.Field()
    cackhoandautu_tcdh = scrapy.Field()
    tongcongtaisan = scrapy.Field()
    nophaitra = scrapy.Field()
    nonganhan = scrapy.Field()
    nodaihan = scrapy.Field()
    duphongnghiepvu = scrapy.Field()
    vochusohuu = scrapy.Field()
    vondautucua_csh = scrapy.Field()
    thangduvon_cp = scrapy.Field()
    loinhuansauthue_chuapp = scrapy.Field()
    loiichcuacongdongthieuso = scrapy.Field()
    tongcongnguonvon = scrapy.Field()

#     Chi so tai chinh
    eps = scrapy.Field()
    bvps= scrapy.Field()
    p_e = scrapy.Field()
    p_b = scrapy.Field()
    tisuatloinhuangopbien = scrapy.Field()
    tisuatsinhloitrendoanhthuthuan = scrapy.Field()
    roea = scrapy.Field()
    roaa = scrapy.Field()
    tisothanhtoanhienhanh = scrapy.Field()
    khanangthanhtoanvaylai = scrapy.Field()
    tisonotrentrongtaisan = scrapy.Field()
    tisonotrenvonchusohuu = scrapy.Field()

