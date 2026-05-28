def print_sample_invitation(mother, father, child, teacher, event):

    # Notice here the use of a multi-line format-string: f''' text here '''
    sample_text = f'''
Dear {mother} and {father}.
{teacher} and I would love to see you both as well as {child} at our {event} tomorrow evening. 

Best regards,
Principal G. Sturgis.
'''
    print(sample_text)

print_sample_invitation('ania', 'jurek','lukasz', 'ktos', 'studiowka')
