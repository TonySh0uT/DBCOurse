import PySimpleGUI as sg
import psycopg2

sg.theme('SystemDefault')
conn = psycopg2.connect(dbname='courseWork', user='postgres',
                        host='localhost', password = '123456')

layoutEditionsView = [[sg.Text('Просмотреть информацию об изданиях')], [sg.Button('Просмотр изданий')]]
layoutPublicationsView = [[sg.Text('Просмотреть публикаций')], [sg.Button('Просмотр публикаций')]]
layoutTranslatorsView = [[sg.Text('Просмотреть список переводчиков')], [sg.Button('Просмотр переводчиков')]]
layoutAgentInsert = [[sg.Text('Добавить агента')], [sg.Button('Добавить агента')]]
layoutAuthorInsert = [[sg.Text('Добавить автора')], [sg.Button('Добавить автора')]]
layoutRedactorInsert = [[sg.Text('Добавить редактора')], [sg.Button('Добавить редактора')]]
layoutPrintingHouseInsert = [[sg.Text('Добавить типографию')], [sg.Button('Добавить типографию')]]
layoutPublicationInsert = [[sg.Text('Добавить публикацию')], [sg.Button('Добавить публикацию')]]
layoutEditionInsert = [[sg.Text('Добавить издание')], [sg.Button('Добавить издание')]]
layoutAgencyInsert = [[sg.Text('Добавить рекламное агенство')], [sg.Button('Добавить рекламное агенство')]]
layoutUpdate = [[sg.Text('Обновить тираж издания')], [sg.Button('Обновить тираж')]]

window = sg.Window('Работа с авторами',
                   (layoutEditionsView, layoutPublicationsView, layoutTranslatorsView,
                    layoutAgentInsert, layoutAuthorInsert, layoutRedactorInsert, layoutPrintingHouseInsert, layoutPublicationInsert, layoutEditionInsert, layoutAgencyInsert, layoutUpdate), size=(350, 670))

while True:
    cursor = conn.cursor()
    cursor.execute("SELECT name from printing_house")
    comlist_printing_houses = cursor.fetchall()
    cursor.execute("SELECT printing_house_id from printing_house")
    indlist_printing_houses = cursor.fetchall()

    cursor.execute("SELECT full_name from translator")
    comlist_translators = cursor.fetchall()
    comlist_translators.append("Нет")
    cursor.execute("SELECT translator_id from translator")
    indlist_translators = cursor.fetchall()

    cursor.execute("SELECT full_name from author")
    comlist_authors = cursor.fetchall()
    cursor.execute("SELECT author_id from author")
    indlist_authors = cursor.fetchall()

    cursor.execute("SELECT name from advertising_agency")
    comlist_number_2 = cursor.fetchall()
    cursor.execute("SELECT agency_id from advertising_agency")
    indlist_number_2 = cursor.fetchall()

    cursor.execute("SELECT full_name from agent")
    comlist_agents = cursor.fetchall()
    cursor.execute("SELECT agent_id from agent")
    indlist_agents = cursor.fetchall()

    cursor.execute("SELECT full_name from editor_in_chief")
    comlist_editors = cursor.fetchall()
    cursor.execute("SELECT editor_id from editor_in_chief")
    indlist_editors = cursor.fetchall()

    cursor.execute("SELECT name from publication")
    comlist_publications = cursor.fetchall()
    cursor.execute("SELECT publication_id from publication")
    indlist_publications = cursor.fetchall()

    cursor.execute("select publication.name from publication join edition on publication.publication_id = edition.publication_id")
    comlist_editions = cursor.fetchall()
    cursor.execute("select edition.edition_id from edition")
    indlist_editions = cursor.fetchall()



    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Добавить агента':
        layout = [
            [sg.Text('Введите необходимые данные')],
            [sg.Text('ФИО', size=(15, 1)), sg.InputText()],
            [sg.Text('Возраст (число)', size=(15, 1)), sg.InputText()],
            [sg.Text('Телефон (+7)', size=(15, 1)), sg.InputText()],
            #[sg.Text('publisher_id', size=(15, 1)),sg.Combo(comlist_prescription_2, size=(15, 1))]
            [sg.Submit()]
        ]
        windowEntry = sg.Window('Окно ввода', layout, keep_on_top=True)
        result = ''
        while True:
            eventEntry, valuesEntry = windowEntry.read()
            if eventEntry == 'Submit':

                try :
                    cursor.execute("insert into agent(full_name, age, phone_number, publisher_id) values ({}, {}, {}, 1);".format( "'" + valuesEntry[0] + "'", valuesEntry[1], "'" + str(valuesEntry[2]) + "'"))
                    conn.commit()

                except (Exception, psycopg2.DatabaseError) as error:
                    print()
                    sg.popup("Ошибка ввода", keep_on_top=True)
                    conn.rollback()
                break

                conn.commit()

                comlist_agents.append(valuesEntry[0])
                cursor.execute("select max(agent_id) from agent")
                num = cursor.fetchall()
                indlist_agents.append(num)
                break

            if eventEntry == sg.WIN_CLOSED:
                break
        windowEntry.close()


    if event == 'Добавить автора':
        layout = [
            [sg.Text('Пожалуйста, введите необходимые данные.')],
            [sg.Text('ФИО', size=(15, 1)), sg.InputText()],
            [sg.Text('Агент'), sg.Combo(comlist_agents, size=(15, 1))],
            [sg.Submit()]
        ]
        windowEntry = sg.Window('Окно ввода', layout, keep_on_top=True)
        result = ''
        while True:
            eventEntry, valuesEntry = windowEntry.read()
            if eventEntry == 'Submit':
                if (str(valuesEntry[0]) != '' and str(valuesEntry[1]) != '' ):
                    cursor.execute("insert into author(full_name, agent_id) values ({}, {});".format(
                             "'" + valuesEntry[0] + "'", comlist_agents.index(valuesEntry[1]) + 1))
                else:
                    sg.popup("Ошибка ввода, какое-то из полей пустое.", keep_on_top=True)
                conn.commit()
                comlist_authors.append(valuesEntry[0])
                cursor.execute("select max(author_id) from author")
                num = cursor.fetchall()
                indlist_authors.append(num)
                break

            if eventEntry == sg.WIN_CLOSED:
                break
        windowEntry.close()


    if event == 'Добавить редактора':
        layout = [
            [sg.Text('Пожалуйста, введите необходимые данные.')],
            [sg.Text('ФИО', size=(15, 1)), sg.InputText()],
            [sg.Text('Возраст', size=(15, 1)), sg.InputText()],
            [sg.Submit()]
        ]
        windowEntry = sg.Window('Окно ввода', layout, keep_on_top=True)
        result = ''
        while True:
            eventEntry, valuesEntry = windowEntry.read()
            if eventEntry == 'Submit':
                if (str(valuesEntry[0]) != '' and str(valuesEntry[1]) != '' ):
                    cursor.execute("insert into editor_in_chief(full_name, age) values ({}, {});".format(
                             "'" + valuesEntry[0] + "'", valuesEntry[1]))
                else:
                    sg.popup("Ошибка ввода", keep_on_top=True)
                conn.commit()
                comlist_editors.append(valuesEntry[0])
                cursor.execute("select max(editor_id) from editor_in_chief")
                num = cursor.fetchall()
                indlist_editors.append(num)
                break

            if eventEntry == sg.WIN_CLOSED:
                break
        windowEntry.close()

    if event == 'Добавить типографию':
        layout = [
            [sg.Text('Пожалуйста, введите необходимые данные.')],
            [sg.Text('Название', size=(15, 1)), sg.InputText()],
            [sg.Text('Адрес', size=(15, 1)), sg.InputText()],
            [sg.Submit()]
        ]
        windowEntry = sg.Window('Окно ввода', layout, keep_on_top=True)
        result = ''
        while True:
            eventEntry, valuesEntry = windowEntry.read()
            if eventEntry == 'Submit':
                if (str(valuesEntry[0]) != '' and str(valuesEntry[1]) != '' ):
                    cursor.execute("insert into printing_house(name, address) values ({}, {});".format(
                             "'" + valuesEntry[0] + "'", "'" + valuesEntry[1] + "'" ))
                else:
                    sg.popup("Ошибка ввода", keep_on_top=True)
                conn.commit()
                comlist_printing_houses.append(valuesEntry[0])
                cursor.execute("select max(printing_house_id) from printing_house")
                num = cursor.fetchall()
                indlist_printing_houses.append(num)
                break

            if eventEntry == sg.WIN_CLOSED:
                break
        windowEntry.close()


    if event == 'Добавить публикацию':
        layout = [
            [sg.Text('Пожалуйста, введите необходимые данные.')],
            [sg.Text('Название', size=(15, 1)), sg.InputText()],
            [sg.Text('Жанр', size=(15, 1)), sg.InputText()],
            [sg.Text('Язык оригинала', size=(15, 1)), sg.InputText()],
            [sg.Text('Главные редактор'), sg.Combo(comlist_editors, size=(15, 1))],
            [sg.Text('Переводчик'), sg.Combo(comlist_translators, size=(15, 1))],
            [sg.Text('Автор'), sg.Combo(comlist_authors, size=(15, 1))],
            [sg.Submit()]
        ]
        windowEntry = sg.Window('Окно ввода', layout, keep_on_top=True)
        result = ''
        while True:
            eventEntry, valuesEntry = windowEntry.read()
            if eventEntry == 'Submit':
                if (str(valuesEntry[0]) != '' and str(valuesEntry[1]) != '' and str(valuesEntry[2]) != '' and str(valuesEntry[3]) != '' and str(valuesEntry[4]) != '' and str(valuesEntry[5]) != ''):
                    cursor.execute("insert into publication(name, genre, origin_language, editor_id) values ({}, {}, {}, {});".format(
                             "'" + valuesEntry[0] + "'", "'" + valuesEntry[1] + "'", "'" + valuesEntry[2] + "'", comlist_editors.index(valuesEntry[3])+1))
                    conn.commit()
                    cursor.execute("select max(publication_id) from publication")
                    num = cursor.fetchone()[0]
                    conn.commit()
                    cursor.execute("insert into author_publication(author_id, publication_id) values ({}, {});".format(comlist_authors.index(valuesEntry[5])+1, num))
                    if(valuesEntry[4] != 'Нет'):
                        conn.commit()
                        cursor.execute("insert into translations(publication_id, translator_id) values ({}, {});".format(num, comlist_translators.index(valuesEntry[4])+1))
                else:
                    sg.popup("Ошибка ввода", keep_on_top=True)
                conn.commit()
                comlist_publications.append(valuesEntry[0])
                cursor.execute("select max(publication_id) from publication")
                num = cursor.fetchall()
                indlist_publications.append(num)
                break

            if eventEntry == sg.WIN_CLOSED:
                break
        windowEntry.close()



    if event == 'Добавить издание':
        layout = [
            [sg.Text('Пожалуйста, введите необходимые данные.')],
            [sg.Text('Тираж', size=(15, 1)), sg.InputText()],
            [sg.Text('Тип издания', size=(15, 1)), sg.InputText()],
            [sg.Text('Публикация'), sg.Combo(comlist_publications, size=(15, 1))],
            [sg.Text('Типография'), sg.Combo(comlist_printing_houses, size=(15, 1))],
            [sg.Submit()]
        ]
        windowEntry = sg.Window('Окно ввода', layout, keep_on_top=True)
        result = ''
        while True:
            eventEntry, valuesEntry = windowEntry.read()
            if eventEntry == 'Submit':
                if (str(valuesEntry[0]) != '' and str(valuesEntry[1]) != '' and str(valuesEntry[2]) != '' and str(valuesEntry[3]) != ''):
                    cursor.execute("insert into edition(amount, edition_type, publication_id, printing_house_id) values ({}, {}, {}, {});".format(valuesEntry[0], "'" + valuesEntry[1] + "'", comlist_publications.index(valuesEntry[2])+1, comlist_printing_houses.index(valuesEntry[3])+1))
                    conn.commit()
                else:
                    sg.popup("Ошибка ввода", keep_on_top=True)
                conn.commit()
                break

            if eventEntry == sg.WIN_CLOSED:
                break
        windowEntry.close()



    if event == 'Добавить рекламное агенство':
        layout = [
            [sg.Text('Пожалуйста, введите необходимые данные.')],
            [sg.Text('Название', size=(15, 1)), sg.InputText()],
            [sg.Text('Адрес', size=(15, 1)), sg.InputText()],
            [sg.Text('Рейтинг', size=(15, 1)), sg.InputText()],

            [sg.Submit()]
        ]
        windowEntry = sg.Window('Окно ввода', layout, keep_on_top=True)
        result = ''
        while True:
            eventEntry, valuesEntry = windowEntry.read()
            if eventEntry == 'Submit':
                if (str(valuesEntry[0]) != '' and str(valuesEntry[1]) != '' and str(valuesEntry[2]) != ''):
                    cursor.execute("insert into advertising_agency(name, address, rating) values ({}, {}, {});".format("'" + valuesEntry[0] + "'", "'" + valuesEntry[1] + "'", valuesEntry[2]))
                    conn.commit()

                    cursor.execute("select max(agency_id) from advertising_agency")
                    num = cursor.fetchone()[0]
                    conn.commit()
                    cursor.execute("insert into advertising_publisher(agency_id, publisher_id) values ({}, 1);".format(num))
                else:
                    sg.popup("Ошибка ввода", keep_on_top=True)
                conn.commit()
                break

            if eventEntry == sg.WIN_CLOSED:
                break
        windowEntry.close()

    if event == 'Просмотр публикаций':
        query = """select publication.name, publication.genre, publication.origin_language, editor_in_chief.full_name from publication
join author_publication on publication.publication_id = author_publication.publication_id join editor_in_chief on editor_in_chief.editor_id = publication.editor_id join author on author_publication.author_id = author.author_id;
"""
        cursor.execute(query)
        data = cursor.fetchall()
        my_data = []
        for i in data:
            my_data.append(list(i))
        headings = ['Название', 'Жанр', 'Язык оригинала', 'ФИО Главного редактора']

        layout = [[sg.Table(values=my_data, headings=headings, max_col_width=35,
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='right',
                            num_rows=20,
                            alternating_row_color='grey',
                            key='-TABLE-',
                            row_height=35)]]

        windowView = sg.Window('Вывод БД', layout)

        while True:
            eventView, valuesView = windowView.read()
            print(eventView, valuesView)
            if eventView == sg.WIN_CLOSED:
                break
        windowView.close()



    if event == 'Просмотр изданий':
        query = """select edition.amount as Количество_копий, edition.edition_type as Тип_издания, publication.name as Описание_издания, publication.genre as Жанр_произведения, author.full_name as Автор from edition, publication,author, author_publication where edition.publication_id = publication.publication_id and author_publication.publication_id = publication.publication_id and author.author_id = author_publication.author_id"""
        cursor.execute(query)
        data = cursor.fetchall()
        my_data = []
        for i in data:
            my_data.append(list(i))
        headings = ['Количество копий', 'Тип издания', 'Описание издания', 'Жанр произведения', 'Автор']

        layout = [[sg.Table(values=my_data, headings=headings, max_col_width=35,
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='right',
                            num_rows=20,
                            alternating_row_color='grey',
                            key='-TABLE-',
                            row_height=35)]]

        windowView = sg.Window('Вывод БД', layout)

        while True:
            eventView, valuesView = windowView.read()
            print(eventView, valuesView)
            if eventView == sg.WIN_CLOSED:
                break
        windowView.close()




    if event == 'Просмотр переводчиков':
        query = """select translator.full_name, translator.age, translator.education from translator;"""
        cursor.execute(query)
        data = cursor.fetchall()
        my_data = []
        for i in data:
            my_data.append(list(i))
        headings = ['ФИО Переводчика', 'Возраст переводчика', 'Образование']

        layout = [[sg.Table(values=my_data, headings=headings, max_col_width=35,
                            auto_size_columns=True,
                            display_row_numbers=True,
                            justification='right',
                            num_rows=20,
                            alternating_row_color='grey',
                            key='-TABLE-',
                            row_height=35)]]

        windowView = sg.Window('Вывод БД', layout)

        while True:
            eventView, valuesView = windowView.read()
            print(eventView, valuesView)
            if eventView == sg.WIN_CLOSED:
                break
        windowView.close()



    if event == 'Обновить тираж':
        idViolation = 0
        layout = [
            [sg.Text('Пожалуйста, введите необходимые данные.')],
            [sg.Text('Издание', size=(15, 1)), sg.Combo(comlist_editions, size=(25, 1))],
            [sg.Text('Новый тираж'), sg.InputText()],
            [sg.Submit()]
        ]
        windowEntry = sg.Window('Окно изменения', layout, keep_on_top=True)
        while True:
            eventEntry, valuesEntry = windowEntry.read()
            if eventEntry == 'Submit':
                edition_id = list(indlist_editions[comlist_editions.index(valuesEntry[0])])[0]
                new_amount = valuesEntry[1]
                break

            if eventEntry == sg.WIN_CLOSED:
                break
        windowEntry.close()
        cursor.execute("update edition set amount = {} " \
                       "where edition_id = {};".format(new_amount, edition_id))
        conn.commit()

        if eventEntry == sg.WIN_CLOSED:
            break
        windowEntry.close()

window.close()
conn.close()