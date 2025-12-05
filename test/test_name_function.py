from name_function import get_formatted_name

def test_first_last_name():
  formatted_name = get_formatted_name('jimi', 'hendrix')
  assert formatted_name == 'Jimi Hendrix'
  
def test_first_last_middle_name():
  formatted_name = get_formatted_name('john', 'hooker', 'lee')
  assert formatted_name == 'John Lee Hooker'