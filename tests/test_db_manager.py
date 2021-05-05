import pytest
from models import DatabaseManager

@pytest.fixture
def database():
    return DatabaseManager()


def test_list_all(database):
    check = database.list_all()
    assert check == [('Igor', 'Wise', '16620315 9220', '1-535-484-7619', '2020-01-15 04:05:37', 'Asset Management'), ('Addison', 'Hurley', '16910913 6391', '1-913-830-6195', '2019-12-24 11:30:44', 'Tech Support'), 
    ('Blaze', 'Torres', '16560621 3386', '1-322-617-4027', '2018-10-14 14:06:56', 'Asset Management'), ('Lane', 'Pate', '16570106 2860', '1-535-631-2216', '2019-09-01 06:29:24', 'Customer Relations'), 
    ('Emerson', 'Grant', '16570524 7400', '1-439-603-8920', '2018-11-24 00:13:45', 'Research and Development'), ('Brian', 'Douglas', '16360128 5707', '1-168-324-7261', '2019-07-20 14:27:05', 'Payroll'), 
    ('Beck', 'Hutchinson', '16230105 8745', '1-513-600-4900', '2019-11-25 01:52:44', 'Public Relations'), ('Hanna', 'Mclaughlin', '16500602 8517', '1-239-125-0408', '2019-07-09 09:31:28', 'Public Relations'), 
    ('Tasha', 'Dejesus', '16510107 4119', '1-973-264-0333', '2019-09-20 13:10:10', 'Sales and Marketing'), ('Kylee', 'Peterson', '16670916 3809', '1-209-712-2748', '2020-03-22 04:39:16', 'Customer Service'), 
    ('Breanna', 'Macdonald', '16260809 4658', '1-653-420-4382', '2018-05-12 23:44:06', 'Tech Support'), ('Kermit', 'Ramirez', '16511206 8738', '1-196-361-7324', '2019-07-01 07:44:38', 'Asset Management'), 
    ('Ursa', 'Mathis', '16470809 2764', '1-956-732-1822', '2019-03-31 18:26:53', 'Tech Support'), ('Galvin', 'Kennedy', '16080115 8205', '1-405-528-6549', '2018-07-28 23:37:39', 'Human Resources'), 
    ('Hedda', 'Cortez', '16640819 8502', '1-534-751-6003', '2018-09-15 02:38:58', 'Quality Assurance'), ('Josiah', 'Hunt', '16330329 3736', '1-463-794-8138', '2019-09-20 04:21:18', 'Payroll'), 
    ('Amaya', 'Yang', '16190813 4081', '1-403-121-5206', '2018-06-15 21:35:42', 'Human Resources'), ('Whitney', 'Savage', '16260703 1925', '1-147-895-1607', '2019-09-15 07:57:45', 'Sales and Marketing'), 
    ('Faith', 'Mccall', '16840911 0940', '1-777-243-8834', '2018-04-22 23:03:35', 'Quality Assurance'), ('Jonas', 'Shelton', '16141114 7471', '1-506-415-6578', '2020-02-09 18:15:02', 'Customer Service'), 
    ('Willow', 'Boyd', '16050508 7858', '1-252-223-4933', '2018-10-13 06:59:39', 'Tech Support'), ('Chaim', 'Montgomery', '16190610 7592', '1-872-989-4205', '2019-10-09 12:59:35', 'Finances'), 
    ('Darrel', 'Mcintosh', '16900127 3144', '1-768-353-8660', '2018-07-10 19:19:09', 'Public Relations'), ('Maxine', 'Stewart', '16180112 1029', '1-226-516-9701', '2018-11-17 08:43:29', 'Accounting'), 
    ('Dominique', 'Watts', '16711026 8666', '1-141-493-3290', '2019-03-04 13:17:28', 'Public Relations'), ('Audrey', 'Barry', '16680428 7297', '1-710-952-9915', '2019-04-04 02:27:40', 'Payroll'), 
    ('April', 'Aguilar', '16670316 6535', '1-423-225-5187', '2019-05-14 07:31:34', 'Research and Development'), ('Ian', 'Rowland', '16620217 2117', '1-570-605-6972', '2018-09-27 06:45:11', 'Asset Management'), 
    ('Colette', 'Flowers', '16040115 0990', '1-440-458-1682', '2019-12-01 00:18:33', 'Finances'), ('Raja', 'Shields', '16080902 2106', '1-402-968-7014', '2018-12-16 00:26:21', 'Human Resources'), 
    ('Levi', 'Mcfadden', '16861129 5067', '1-462-109-3021', '2018-05-11 15:41:27', 'Customer Relations'), ('Joseph', 'Lawrence', '16520804 3413', '1-625-738-3900', '2019-06-15 21:41:45', 'Customer Relations'), 
    ('Rachel', 'Rodriguez', '16240305 2232', '1-503-927-7539', '2018-07-06 18:31:24', 'Human Resources'), ('Quinn', 'Terry', '16880217 0582', '1-252-916-2118', '2020-01-06 22:29:17', 'Legal Department'), 
    ('Reese', 'Little', '16200622 5474', '1-699-434-5781', '2018-07-16 14:18:40', 'Finances'), ('Chava', 'Higgins', '16301027 9879', '1-798-330-8528', '2019-01-17 10:29:09', 'Tech Support'), 
    ('Althea', 'Knowles', '16080919 2610', '1-102-218-5251', '2019-09-05 07:19:13', 'Human Resources'), ('Tatum', 'Klein', '16080729 8948', '1-888-715-3533', '2020-02-07 05:56:50', 'Advertising'), 
    ('CassIDnumbery', 'Ratliff', '16750212 8627', '1-370-533-1484', '2018-09-30 06:17:01', 'Advertising'), ('Garth', 'Clay', '16890404 8538', '1-877-337-5794', '2019-05-24 17:08:31', 'Research and Development'), 
    ('Giacomo', 'Frederick', '16150507 1496', '1-987-496-4999', '2018-11-19 06:32:55', 'Public Relations'), ('Justin', 'Huffman', '16380323 8298', '1-466-303-7057', '2018-10-04 06:49:15', 'Human Resources'), 
    ('Mannix', 'Brock', '16150219 7203', '1-895-348-1142', '2018-08-28 03:13:47', 'Human Resources'), ('Castor', 'Bennett', '16730226 2261', '1-247-432-2925', '2019-02-08 10:07:41', 'Legal Department'), 
    ('Kiayada', 'Mercer', '16380812 6977', '1-411-251-9362', '2020-04-05 21:31:21', 'Finances'), ('Dakota', 'Colon', '16520610 4969', '1-351-215-4060', '2019-11-05 20:06:06', 'Customer Relations'),
     ('Hamish', 'Rodriguez', '16460925 1402', '1-169-412-0601', '2019-06-06 13:21:13', 'Customer Service'), ('Vernon', 'Lloyd', '16530304 9786', '1-831-349-5502', '2019-06-29 10:42:48', 'Legal Department'), 
     ('Arthur', 'Conley', '16090317 8150', '1-483-245-6233', '2020-03-18 05:28:33', 'Legal Department'), ('Lana', 'Vargas', '16930204 4590', '1-462-230-1065', '2020-02-16 19:24:49', 'Accounting'), 
     ('Colby', 'Bray', '16300908 1229', '1-173-866-9740', '2020-04-09 12:30:12', 'Accounting'), ('Talon', 'Nieves', '16110826 3847', '1-450-457-5631', '2018-10-20 07:02:48', 'Asset Management'), 
     ('Giacomo', 'Townsend', '16230218 3286', '1-172-878-3369', '2020-02-02 00:41:00', 'Finances'), ('Zahir', 'Ratliff', '16660308 3129', '1-949-285-6015', '2019-12-30 16:46:52', 'Asset Management'), 
     ('Julian', 'Hinton', '16310430 8956', '1-697-901-4881', '2019-01-11 22:07:06', 'Sales and Marketing'), ('Elton', 'Salinas', '16990811 6552', '1-490-215-0358', '2020-01-11 22:17:10', 'Public Relations'), 
     ('Shay', 'Church', '16210912 1679', '1-758-746-4869', '2019-08-22 11:06:58', 'Accounting'), ('Gage', 'Jacobs', '16751021 8147', '1-760-284-8191', '2019-08-01 13:11:43', 'Sales and Marketing'), 
     ('Ariana', 'Mcconnell', '16640917 7299', '1-255-964-5876', '2019-11-28 07:58:41', 'Legal Department'), ('Cheyenne', 'Mccall', '16541204 7648', '1-969-750-3899', '2018-07-21 03:57:13', 'Tech Support'), 
     ('Maris', 'Boone', '16170307 5661', '1-206-191-8088', '2019-06-29 11:57:42', 'Sales and Marketing'), ('Ciara', 'Delgado', '16560216 7701', '1-852-740-2974', '2019-04-02 08:09:28', 'Tech Support'), 
     ('Margaret', 'Cohen', '16370313 2757', '1-454-283-6466', '2019-07-04 15:27:06', 'Public Relations'), ('Silas', 'Murray', '16860120 6512', '1-665-745-2503', '2019-08-08 23:05:31', 'Finances'), 
     ('Leah', 'Compton', '16430708 1382', '1-567-649-6972', '2018-05-12 21:01:14', 'Payroll'), ('Ava', 'Taylor', '16180721 4539', '1-612-754-2143', '2018-06-02 23:43:37', 'Quality Assurance'), 
     ('Tobias', 'Scott', '16290414 9495', '1-176-773-3928', '2019-10-23 23:15:07', 'Research and Development'), ('Asher', 'Chan', '16370507 7372', '1-931-492-0935', '2019-10-21 22:41:22', 'Finances'), 
     ('Sloane', 'Hinton', '16660712 0117', '1-945-589-6680', '2019-04-27 22:07:42', 'Legal Department'), ('Cathleen', 'Barlow', '16081113 1713', '1-613-340-5124', '2020-03-16 18:24:27', 'Quality Assurance'), 
     ('Moses', 'Cantrell', '16040804 9864', '1-461-740-9141', '2018-05-13 23:59:40', 'Sales and Marketing'), ('Alexandra', 'Maxwell', '16000101 0859', '1-102-835-0632', '2019-06-04 21:57:32', 'Tech Support'), 
     ('Elijah', 'Mason', '16050327 8467', '1-273-916-8684', '2019-06-28 16:07:25', 'Media Relations'), ('Francis', 'Atkins', '16031124 3000', '1-387-886-7353', '2019-09-20 15:42:27', 'Media Relations'), 
     ('Buckminster', 'Greer', '16670813 4892', '1-358-678-3762', '2018-05-10 22:21:57', 'Tech Support'), ('Macaulay', 'Rodgers', '16400202 0180', '1-947-613-5172', '2019-03-23 09:05:17', 'Media Relations'), 
     ('Yetta', 'Whitfield', '16290208 1724', '1-969-658-9134', '2018-08-09 04:03:15', 'Media Relations'), ('Isaiah', 'Jenkins', '16520921 5580', '1-936-512-2949', '2019-02-03 23:15:38', 'Advertising'), 
     ('Regina', 'Gomez', '16800109 5739', '1-547-104-8661', '2018-06-09 16:48:36', 'Sales and Marketing'), ('Camilla', 'Gibson', '16851216 1343', '1-186-857-8580', '2018-07-29 11:32:29', 'Payroll'), 
     ('Julian', 'Rodriquez', '16280923 0879', '1-112-208-9800', '2018-07-13 10:06:55', 'Tech Support'), ('Price', 'Crawford', '16681023 1743', '1-565-139-5739', '2018-12-15 13:15:32', 'Human Resources'), 
     ('Ciaran', 'Cole', '16121003 0852', '1-738-719-9990', '2019-03-10 17:19:37', 'Customer Relations'), ('Desiree', 'Morgan', '16101115 8472', '1-153-178-5627', '2019-11-26 08:36:21', 'Tech Support'), 
     ('Jescie', 'Washington', '16340607 7085', '1-280-571-0184', '2020-04-03 04:28:47', 'Tech Support'), ('Anthony', 'Dennis', '16240916 4544', '1-547-435-5293', '2019-01-09 06:03:32', 'Legal Department'), 
     ('Lilah', 'Maddox', '16400704 1314', '1-420-588-8987', '2018-12-19 01:50:49', 'Media Relations'), ('Breanna', 'Cooper', '16891216 4442', '1-307-713-1816', '2019-12-30 04:57:55', 'Accounting'), 
     ('Wilma', 'Alston', '16420711 4168', '1-299-941-1533', '2018-08-07 09:42:43', 'Tech Support'), ('Chaim', 'Scott', '16880429 8043', '1-109-665-9476', '2018-12-01 18:28:16', 'Customer Service'), 
     ('Grant', 'Love', '16090928 7609', '1-524-363-2880', '2020-03-03 09:36:36', 'Customer Relations'), ('Chadwick', 'Hutchinson', '16630610 0527', '1-394-673-5483', '2018-05-31 11:52:05', 'Advertising'), 
     ('Kelly', 'Rivera', '16580601 9633', '1-875-188-3621', '2018-09-19 16:12:25', 'Payroll'), ('Joseph', 'Morton', '16431114 2089', '1-838-333-2241', '2019-04-04 22:10:58', 'Media Relations'), 
     ('Jesse', 'Lindsey', '16840117 9034', '1-583-753-4219', '2018-07-11 23:56:40', 'Sales and Marketing'), ('Keane', 'Woods', '16790621 1896', '1-296-738-3520', '2020-02-05 11:09:39', 'Customer Service'), 
     ('Martha', 'Freeman', '16291118 1812', '1-632-539-0135', '2020-02-24 08:39:00', 'Quality Assurance'), ('Uriel', 'Cleveland', '16940624 7016', '1-483-523-5114', '2018-04-16 15:03:29', 'Media Relations'), 
     ('Rigel', 'Henry', '16240222 3909', '1-676-917-1539', '2020-02-08 21:40:16', 'Accounting'), ('Charles', 'Copeland', '16520606 9428', '1-332-502-0313', '2018-05-21 17:58:32', 'Legal Department')]


def test_return_one(database, number='16291118 1812'):
    check = database.return_one(number)
    assert check == ('Martha', 'Freeman', '16291118 1812', '1-632-539-0135', '2020-02-24 08:39:00', 'Quality Assurance')


def test_error_return_one(database, number='1'):
    check = database.return_one(number)
    assert check == None