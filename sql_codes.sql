/* question 1 */
INSERT INTO account_users  (
        password, username  , first_name ,
        last_name , email,is_superuser,is_staff , 
        is_active , date_joined)
VALUES ('123' , 'user1', 'mohammad' ,
        'yousefian' , 'a@gmail.com' ,
        'False' ,'False' , 'False' , 
        '2023-01-01 12:43:22.690778+03:30');  /* create user */

INSERT INTO account_phones (phone)
VALUES ('9124890654');   /* create phone number */

INSERT INTO account_driver (gender , type ,phone_id , user_id ,charge, history,rate)
     SELECT 'MALE' , 'Client' , account_phones.id ,
      account_users.id , 0 , 'no-history' , 0
      FROM account_phones ,account_users WHERE phone = '9124890654'
      AND username = 'user1';         /* create client */ 
/* End Question 1 */










/* question 2 */
UPDATE account_users 
SET password = '321'
WHERE username = 'user1';               /* change password of user1 */
/* End Question 2 */









/* question 3 */
SELECT * FROM account_driver
WHERE type = 'Client' AND rate = 0;
/* End Question 3 */








/* question 4 */
SELECT * FROM account_driver
WHERE type = 'Client' AND username = 'user1' AND password = '321';
/* End Question 4 */








/* question 5 */
INSERT INTO main_requestclient( 
        req_start, req_time_start ,
        start_loc,finish_loc, client_id ,
        distance , estimated_time ,  finish_loc_lat   ,
        start_loc_lat , start_loc_lon ,   finish_loc_lon   ,
        text_address_start , text_address_finish )

VALUES (
         '2023-01-10' , '19:27:20.30037' , '0101000020E610000017F032C346AB49402D5E2C0C91D94140' , '0101000020E6100000B
        A065ECF0EA74940383AA24388DA4140' ,19 ,4651 ,473 , '35.70728345319043' ,'35.699739' ,'51.3380
        1',51.305139466201084 , 'تهران، میدان آزادی', 'تهران، گلزار'
);
/* End Question 5 */












/* question 6 */
INSERT INTO main_car( 
        color , model , number_plate_first_part ,
        number_plate_second_part , number_plate_third_part ,
        number_plate_forth_part , driver_id ,type
)

VALUES(
          'سفید','2022-12-27', '17', 'م', '141', '33',18,'pride'
);
/* End Question 6 */













/* question 7 */
INSERT INTO account_users  (
        password, username  , first_name ,
        last_name , email,is_superuser,is_staff , 
        is_active , date_joined)
VALUES ('123' , 'driver1', 'gholam' ,
        'gholami' , 'a@gmail.com' ,
        'False' ,'False' , 'False' , 
        '2023-01-01 12:43:22.690778+03:30');  /* create user */

INSERT INTO account_phones (phone)
VALUES ('9124890655');   /* create phone number */

INSERT INTO account_driver (gender , type ,phone_id , user_id ,charge, history,rate)
     SELECT 'MALE' , 'Driver' , account_phones.id ,
      account_users.id , 0 , 'no-history' , 0
      FROM account_phones ,account_users WHERE phone = '9124890655'
      AND username = 'driver1';         /* create client */ 
/* End Question 7 */









/* question 8 */
/* name of a driver with a request of n */
SELECT account_users.username FROM account_driver
INNER JOIN account_users  ON account_users.id = account_driver.user_id
INNER JOIN main_requestdriver ON main_requestdriver.driver_id = account_driver.id
WHERE main_requestdriver.id = 77;
/* End Question 8 */












/* question 9 */
INSERT INTO main_trip( 
        distance ,start_time,
        driver_id , passenger_id , 
        status  , req_driver_id , req_passenger_id 
)
VALUES(
          4358 , '2023-01-17 10:18:14.178041+03:30' ,31 ,30 , 'STARTED' ,77 ,220

);
/* End Question 9 */












/* question 10 */
/* name of a driver and client with a trip of n */
SELECT username FROM main_trip , account_users ,account_driver
WHERE main_trip.id = 110 AND account_users.id = account_driver.user_id;
/* End Question 10 */













/* question 11 */
DELETE FROM account_driver
WHERE rate < 5;
/* End Question 11 */









/* question 12 */
DELETE FROM account_driver WHERE account_driver.id NOT IN(
        SELECT main_trip.driver_id FROM main_trip 
        WHERE main_trip.driver_id = account_driver.id AND account_driver.type = 'Driver'

);
/* End Question 12 */










/* question 13 */
DELETE FROM account_driver WHERE account_driver.id NOT IN(
        SELECT main_trip.passenger_id FROM main_trip 
        WHERE  main_trip.passenger_id = account_driver.id AND account_driver.type = 'Client'
);
/* End Question 13 */







/* question 14 */
/* delete account */
DELETE FROM account_users 
WHERE username = 'user1';
/* End Question 14 */










/* question 15 */
UPDATE main_car 
SET model = 'pezho' , color = 'white'
WHERE main_car.id IN (SELECT car_id FROM account_driver WHERE account_driver.id = 1);
/* End Question 15 */









/* question 16 */
SELECT * FROM main_trip WHERE distance = 20;
/* End Question 16 */









/* question 17 */
SELECT account_users.username FROM account_users , account_driver , main_trip
WHERE account_users.id = account_driver.user_id AND
        main_trip.distance = 20 AND
        main_trip.driver_id = account_driver.id;
/* End Question 17 */







/* question 18 */
UPDATE main_trip 
SET distance = 30 
WHERE distance = 20;
/* End Question 18 */









/* question 19 */
UPDATE account_users
set email = 'a@a.com'
WHERE username  = 'user1'
/* End Question 19 */










/* question 20 */
UPDATE account_users 
SET email = NULL
WHERE username = 'user1'
/* End Question 20 */




