# Glossary 2: Clean up the code from the previous exercise "Glossary" by replacing your series of print()
# calls with a loop that runs through the dictionary's keys and values. 
# When you're sure that your loop works, add five more Python terms to your glossary. When you run your
# program again, these new words and meanings should automatically be included in the output.


programming_glossary =  {
    'Loop': 'Where you can perform a task for values for example in a list, tuple or dictionary',
    'Tuple': 'A list that essentially cannot be modified',
    'List': 'A collection of items in a particular order',
    'If Statement': 'A condition that allows you perform an action depending boolean value being executed',
    'List Comprehension': 'Refactoring code block into one line. Often seen in lists'
}

for term, description in programming_glossary.items():
    print(f'{term} - {description}')