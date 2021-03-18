from requests_html import HTMLSession

url = 'https://sh.zu.fang.com/'
param = 'house/i3'
url2="https://easyai.tech/ai-definition/tf-idf/"


# url = 'https://www.baidu.com/'

def handler_data(s, my_cursor):
    print(type(s))
    info = s.html.find('.info')

    for i in info:
        title = '\'' + i.find('p')[0].text + '\''
        desc = '\'' + i.find('p')[1].text + '\''
        where = '\'' + i.find('p')[2].text + '\''
        who = '\'' + i.find('p')[4].text + '\''
        money = '\'' + i.find('div')[1].text + '\''
        mmm = (r'insert into zu_fang(title,description,address,from_where,money)values('
               + title + ',' + desc + ',' + where + ',' + who + ',' + money + ')')
        # print(mmm)
        my_cursor.execute(mmm)


def spider(my_cursor):
    session = HTMLSession()
    response = session.get(url)
    handler_data(response, my_cursor)
    for i in range(2, 50):
        nurl = url + param + str(i) + '/?rfss=2-95c3bc3aad13ac860a-a5#'
        nresponse = session.get(nurl)
        handler_data(nresponse, my_cursor)


def getUrl():
    html_session = HTMLSession()
    resp = html_session.get(url2)
    info = resp.html.find(".item-link-inner")
    for i in info:
        print(i.find('a')[0].text,i.find('a')[0].links,'\n')


if __name__ == '__main__':
    # abspath = os.path.abspath(os.path.dirname(__file__))
    # t = open(abspath + '/mysql.yml')
    # temp = yaml.load(t.read(), Loader=yaml.FullLoader)
    # conn = sql_con.mysql.get_mysql(temp)
    # my_cursor = conn.cursor()
    # spider(my_cursor)
    # conn.commit()
    getUrl()
