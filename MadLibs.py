from random import randint
done = False

while not done:
    print ("""Welcome to my madlibs game! 
    You be asked for differant parts of speech to fill
    in the paragraph. 
    Have Fun!""")
    #chosen_madlib = randint(1, 4)
    #if chosen_madlib == 1:
    plural_noun1 = raw_input ("Please give a plural noun ")
    plural_noun2 = raw_input ("Please give a plural noun ")
    part_of_the_body1 = raw_input ("Please give a part of the body ")
    number = raw_input ("Please give a number ")
    plural_noun3 = raw_input ("Please give a plural noun")
    part_of_the_body2 = raw_input ("Please give a part of the body ")
    type_of_liquid1 = raw_input ("Please give a type of liquid ")
    type_of_liquid2 = raw_input ("Please give a type of liquid ")
    plural_part_of_the_body1 = raw_input ("Please give a part of the body(plural) ")
    part_of_the_body3 = raw_input ("Please give a part of the body ")
    plural_part_of_the_body2 = raw_input ("Please give a plural part of the body(plural ")
    plural_noun4 = raw_input ("Please give a plural noun" )
    adjective1 = raw_input ("Please give an adjective" )
    adjective2 = raw_input ("Please give an adjective" )
    verb_ending_in_ing  = raw_input ("Please give a verb_ending in -ing" )
    noun1 = raw_input ("Please give a noun" )
    verb1 = raw_input ("Please give a verb")
    plural_noun5 = raw_input ("Please give a plural noun" )
    noun2 = raw_input ("Please give a noun" )
    
    madlib1 = ("""Giraffes heve aroused the curiosity of %s since the earliest of times.
    The giraffe is the tallest of all living %s, but scientists are unabke ti explain how it got it's long neck
    The girraffe's tremendous height, which might reach %s %s, comes mostly from it's legs and long %s. 
    If a giraffe wants to have a drink of %s from the ground, it has to spread it's %s far apart and lap up the %s with it's huge %s. 
    The giraffe has huge %s that are sensative to the faintest %s, and a/an %s sense of of smell and sight. 
    When attacked, the giraffe can put up a/an %s by %s out with i's hind legs and using it's head like a/an %s. Finally, a giraffe can %s at more than thirty %s an hour
    when purused and can outrun the fastest %s.""")
    print madlib1 %(plural_noun1, plural_noun2, part_of_the_body1, number, plural_noun3, part_of_the_body2,type_of_liquid1, type_of_liquid2, plural_part_of_the_body1, part_of_the_body3, plural_part_of_the_body2, plural_noun4,adjective1, adjective2, verb_ending_in_ing, noun1, verb1, plural_noun5)
    
    quit_input = raw_input("Do you want to play again? Yes or No")
    if quit_input == ("No"):
        done = True
    else:
        done = False