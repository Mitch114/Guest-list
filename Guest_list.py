#creating list and invitations
guest_names = ['Mark Z', 'Bill Gates', 'Elon Musk']
friend = guest_names.pop(0)
print(f"You are invited to dinner {friend}.")

guest_names = ['Mark Z', 'Bill Gates', 'Elon Musk']
friend = guest_names.pop(1)
print(f"You are invited to dinner {friend}.")

guest_names = ['Mark Z', 'Bill Gates', 'Elon Musk']
friend = guest_names.pop(2)
print(f"You are invited to dinner {friend}.")

#uninvite Bill
print('Bill gates is no longer able to attend')

#replace Bill with Stevo
guest_names = ['Mark Z', 'Bill Gates', 'Elon Musk']
print(guest_names)

guest_names[1] = 'Stevo'
print(guest_names)

#invite guests indivdually
guest_names = ['Mark Z', 'Stevo', 'Elon Musk']
friend = guest_names.pop(0)
print(f"You are invited to dinner {friend}.")

guest_names = ['Mark Z', 'Stevo', 'Elon Musk']
friend = guest_names.pop(1)
print(f"You are invited to dinner {friend}.")

guest_names = ['Mark Z', 'Stevo', 'Elon Musk']
friend = guest_names.pop(2)
print(f"You are invited to dinner {friend}.")


print('Attention, we have found a bigger dinner table')

#add guests using insert()
guest_names = ['Mark Z', 'Stevo', 'Elon Musk']
guest_names.insert(0, 'Jonny K')
print(guest_names)

guest_names = ['Jonny K ',  'Mark Z', 'Stevo', 'Elon Musk']
guest_names.insert(2, 'Bam')
print(guest_names)

#add guest using append()
guest_names = ['Jonny K ',  'Mark Z', 'Bam', 'Stevo', 'Elon Musk']
guest_names.append('Trump')
print(guest_names)

#invite all guests using pop()
guest_names = ['Jonny K ',  'Mark Z', 'Bam', 'Stevo', 'Elon Musk']
friend = guest_names.pop(0)
print(f"You are invited to the new dinner party {friend}!")

guest_names = ['Jonny K ',  'Mark Z', 'Bam', 'Stevo', 'Elon Musk']
friend = guest_names.pop(1)
print(f"You are invited to the new dinner party {friend}!")

guest_names = ['Jonny K ',  'Mark Z', 'Bam', 'Stevo', 'Elon Musk']
friend = guest_names.pop(2)
print(f"You are invited to the new dinner party {friend}!")

guest_names = ['Jonny K ',  'Mark Z', 'Bam', 'Stevo', 'Elon Musk']
friend = guest_names.pop(3)
print(f"You are invited to the new dinner party {friend}!")

guest_names = ['Jonny K ',  'Mark Z', 'Bam', 'Stevo', 'Elon Musk']
friend = guest_names.pop(4)
print(f"You are invited to the new dinner party {friend}!")

guest_names = ['Jonny K ',  'Mark Z', 'Bam', 'Stevo', 'Elon Musk', 'Trump']
friend = guest_names.pop(5)
print(f"You are invited to the new dinner party {friend}!")

print('Unfortunitly, everyone except for two people got to go')

#remove guests using pop()
guest_names = ['Jonny K ',  'Mark Z', 'Bam', 'Stevo', 'Elon Musk', 'Trump']
popped_guest = guest_names.pop(5)
print(popped_guest, 'you are no longer invited')

guest_names = ['Jonny K ',  'Mark Z', 'Bam', 'Stevo', 'Elon Musk']
popped_guest = guest_names.pop(3)
print(popped_guest, 'you are no longer invited')

guest_names = ['Jonny K ',  'Mark Z', 'Bam', 'Elon Musk']
popped_guest = guest_names.pop(0)
print(popped_guest, 'you are no longer invited')

guest_names = ['Mark Z', 'Bam', 'Elon Musk']
popped_guest = guest_names.pop(1)
print(popped_guest, 'you are no longer invited')

guest_names = ['Mark Z', 'Elon Musk']
print(guest_names, 'you guys are still invited!')

guest_names = ['Mark Z', 'Elon Musk']
print(guest_names)

#remove last guest using del()
del guest_names[1]
print(guest_names)

guest_names = ['Mark Z']

del guest_names[0]
print(guest_names)

#using slices
guest_names = ['Mark Z', 'Bill Gates', 'Elon Musk']

print("Here is the first guest on the list:")
for guest in guest_names[:1]:
    print(guest.title())

guest_names = ['Mark Z', 'Bill Gates', 'Elon Musk']

print("Here are the next guests on the list:")
for guests in guest_names[1:3]:
    print(guests.title())    
