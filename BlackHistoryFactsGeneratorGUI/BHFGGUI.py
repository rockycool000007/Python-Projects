"""
Title: Black History Facts Generator
Creator: Brittany Gates (github.com/bcgates82 / twitter.com/brittanygates82)
About: In celebration of Black History Month I've created a random Black History Facts generator.
Fact Sources:
http://www.history.com/topics/black-history/black-history-facts
http://www.history.com/topics/black-history/black-history-milestones
http://www.history.com/topics/black-history/booker-t-washington
http://www.history.com/topics/black-history/george-washington-carver
https://en.wikipedia.org/wiki/W._E._B._Du_Bois
"""

import tkinter
import random


# The function that displays a random fact
def random_fact():

    global fact_frame

    random.choice(black_history_facts)
    fact_frame.destroy()
    # The facts frame
    fact_frame = tkinter.Frame(m_window)
    fact_frame.grid(row=2, column=0)
    # The text bar displaying the facts
    fact_display = tkinter.Message(fact_frame, text=random.choice(black_history_facts) +
                                   '\n\nHow was this fact generated? Learn here: '
                                   ' https://github.com/bcgates82')
    fact_display.grid(row=0, column=0)


# The list containing the facts
black_history_facts = [
    'Black History Month began as "Negro History Week," which was created in 1926 by Carter G. Woodson.',
    'Black History Month became a month-long event in 1976.',
    'The month of February was chosen for Black History Month to coincide with the birthdays '
    + 'of Frederick Douglass and Abraham Lincoln.',
    'The National Association for the Advancement of Colored People (NAACP) was formed in 1908 ' +
    'by a group of African-American leaders.',
    'Jack Johnson became the first black man to hold the World Heavyweight Champion boxing title ' +
    'in 1908. He held on to the belt until 1915.',
    'John Mercer Langston was the first black man to become a lawyer in Ohio when he passed the Bar in 1854.',
    'John Mercer Langston was elected to the post of Town Clerk for Brownhelm, Ohio in 1855 ' +
    'and became one of the first black people elected to public office in America.',
    'Thurgood Marshall was the first black person ever appointed to the United States Supreme Court. ' +
    'He served from 1967 to 1991.',
    'George Washington Carver developed 300 derivative products from peanuts.',
    'Hiram Rhodes Revels was the first black person ever elected to the U.S. Senate. ' +
    'He represented the state of Mississippi from February 1870 to March 1871.',
    'In 1968 Shirley Chisholm was the first black woman elected to the House of Representatives, ' +
    'representing the state of New York.',
    'In 1972 Shirley Chisholm was the first major party black candidate and first female candidate for U.S. president.',
    'In 1940, Hattie McDaniel was the first black performer to win an Academy Award ' +
    'for her role of a slave governess in "Gone With the Wind".',
    'In 1992, Dr. Mae Jemison became the first black woman to go into space aboard the space shuttle Endeavor.',
    'In 1831, Nat Turner led the only effective slave rebellion in the U.S.',
    'Harriet Tubman helped about 300 slaves escape to the North with the Underground Railroad. ' +
    'Then she served as a scout and spy for the Union during the Civil War.',
    'Booker T. Washington founded the Tuskegee Institute in 1881 to train teachers.',
    'Booker T. Washington served as an adviser to President Theodore Roosevelt and President Taft.',
    'Although George Washington Carver is best known for his work with peanuts, ' +
    'his main contribution to science was his teachings of sustainable agriculture.',
    'W.E.B. Du Bois was the leader of the Niagara Movement which fought for full civil rights for black people.',
    'About 500,000 black men served overseas during WWII. Over 3 million signed up for service.',
    'Dorie Miller, a Navy steward on the U.S.S. West Virginia, carried wounded crewmembers to safety ' +
    'and shot down several Japanese planes. He became the first black hero from WWII.',
    'The Tuskegee Institute graduated the first all-black military aviation program in 1943. ' +
    'They became later known as the "Tuskegee Airmen."',
    'Captain Benjamin O. Davis Jr., who led the Tuskegee Airmen, later became the first black general.',
    'The Tuskegee Airmen flew over 3,000 missions and fought against the Germans and Italians.',
    'Jackie Robinson played his first MLB game on April 15, 1947 with the Brooklyn Dodgers, ' +
    'becoming the first black person to play in the MLB.',
    'Emmett Till\'s murder in 1955, and the hasty acquittal of the two white men who killed Tate, ' +
    'helped bring about the Civil Rights movement.',
    'The city-wide bus boycott in Montgomery, AL began in 1955 after Rosa Parks was arrested for refusing ' +
    'to give up her seat to a white man and move to the back of the bus.',
    'The Montgomery Bus Boycott almost drove the affected bus company into bankruptcy as black ' +
    'citizens made nearly 70 percent of the company\'s customers.',
    'The "Sit-In" Movement started after 4 black college students were refused service at ' +
    'the whites-only counter at a local Woolworth\s in Greensboro, NC.',
    'The "Sit-In" Movement help create the Student Noviolent Coordinating Committee (SNCC) ' +
    'in 1960. They participated in "Freedom Rides" and the March on Washington.',
    'The 13th Amendment officially abolished slavery in the United States.',
    'The 14th Amendment provided equal protection of the Constitution to former slaves.',
    'The 15th Amendment guaranteed a citizen\'s right to vote, no matter race, ' +
    'color or former servitude.',
    'President Harry S. Truman integrated the U.S. Armed Forces in 1948 under an executive order.',
    'Civil rights leader James Farmer started the Congress of Racial Equality (CORE) ' +
    'in 1942 to end discrimination and improve race relations through action.',
    'CORE staged sit-ins in Chicago (pre-dating the sit-ins in the 1960s) ' +
    'and integrated bus rides through the upper South in 1947.',
    'Due to CORE\'s actions with other civil rights groups, the Interstate Commerce Commission ' +
    'mandated all interstate bus carriers could not require required segregated terminals or buses.',
    'Air-Force veteran James Meredith successfully sued the University of Mississippi ' +
    'to be admitted to the university in 1962.',
    'About 250,000 people (black and white) participated in the March on Washington in 1963.',
    'The March on Washington called for voting rights, equal employment opportunities ' +
    'for blacks and to end racial segregation.',
    'Dr. Martin Luther King, Jr. presented and read his famous "I Have a Dream" speech ' +
    'at the March on Washington in 1963.',
    'President Lyndon B. Johnson signed the Civil Rights Act in 1964, giving the federal government ' +
    'more power to protect all citizens against discrimination.',
    'The Civil Rights Act created the Equal Employment Opportunity Commission (EEOC). ' +
    'It was to ensure equal treatment of minorities in the workplace.',
    'Malcolm X\'s Autobiography laid the foundation for the Black Power movement ' +
    'starting in the late 1960s.',
    'Malcolm X was assassinated on February 21, 1965 at a speaking engagement in Harlem ' +
    'by three members of the Nation of Islam.',
    'President Lyndon B. Johnson called for federal legislation to protect voting rights for Blacks ' +
    'after seeing the protestors marching to Selma, AL. The result was the passage of the Voting Rights Act in 1965.',
    'The Voting Rights Act banned illegal voting barriers at the state level, such as literacy tests.',
    'The term "Black Power" was coined by Stokely Carmichael, the then-SNCC ' +
    '(Student Nonviolent Coordinating Committee) chairman in 1966.',
    'The Black Panther Party was created in 1966 by Huey P. Newton and Bobby Seale, ' +
    'college students in Oakland, CA.',
    'The original theme behind the Black Panther Party was to protect black people from ' +
    'attacks from white people through patrolling black neighborhoods.',
    'The Fair Housing Act of 1968 was to address racial discrimination in the sale, ' +
    'rental and financing of housing units.',
    'Martin Luther King Jr. was assassinated on April 4, 1968 at a motel in Memphis, TN by James Earl Ray.',
    'Colin Powell became the first black Chairman of the Joint Chiefs of Staff in 1989. ' +
    'He later became the first black Secretary of State in 2001.',
    'Condoleeza Rice became the first black woman Secretary of State in 2004.',
    'Barack Obama was inaugurated the first black U.S. President in 2009.'
]

m_window = tkinter.Tk()

# Setup the main window and frames for the facts
m_window.title('Black History Facts Generator')
m_window.geometry('400x300')

# The background image for the main window
bg_image = tkinter.PhotoImage(file='nmaahc_credit_alankarchmer_222.gif')
background_label = tkinter.Label(m_window, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# The button frame
button_frame = tkinter.Frame(m_window)
button_frame.grid(row=1, column=0)

# The button to display more facts
fact_button = tkinter.Button(button_frame, text='Next Fact', command=random_fact)
fact_button.grid(row=2, column=1)

# The facts frame
fact_frame = tkinter.Frame(m_window)
fact_frame.grid(row=2, column=0)

# The text bar displaying the initial fact
initial_fact_display = tkinter.Message(fact_frame, text=random.choice(black_history_facts) +
                                       '\n\nHow was this fact generated? Learn here: '
                                       ' https://github.com/bcgates82')
initial_fact_display.grid(row=0, column=0)

m_window.mainloop()
