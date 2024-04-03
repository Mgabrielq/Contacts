
contacts = {
    'number': 4,
    'students':
        [
            {'name':'Sara Holderness', 'email':'sarah@example.com'},
            {'name':'harry Potter', 'email':'harry@example.com'},
            {'name':'Hermione Granger', 'email':'hermione@example'},
            {'name':'Ron Wasley', 'email':'ron@example.com'}
        ]      
}

print('Student email:')
for student in contacts['students']:
    print(student['email'])