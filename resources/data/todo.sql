USE `flask`;

DROP TABLE IF EXISTS `todo`;
DROP TRIGGER IF EXISTS `todo_before_new_todo`;
CREATE TABLE `todo`
(
    `id`          VARCHAR(20) NOT NULL,
    `name`        VARCHAR(20),
    `description` VARCHAR(120),
    `content`     VARCHAR(10000),
    `created_on`  DATETIME,
    `modified_on` DATETIME,
    PRIMARY KEY (`id`)
);

DELIMITER $$
CREATE DEFINER = CURRENT_USER TRIGGER `todo_before_new_todo`
    BEFORE INSERT
    ON `todo`
    FOR EACH ROW
BEGIN
    DECLARE `count` INT;
    SET `count` = (SELECT COUNT(*) FROM `flask`.`todo`);
    SET `new`.`id` = uuid_short();
    SET `new`.`modified_on` = NULL;
    IF `NEW`.`name` IS NULL
    THEN
        SET `new`.`name` = concat('Untitled-', `count` + 1);
    END IF;
    IF `new`.`created_on` IS NULL
    THEN
        SET `new`.`created_on` = CURRENT_TIMESTAMP;
    END IF;
END $$

INSERT INTO `todo` (`name`, `description`, `content`)
VALUES ('todo 1', 'some description for todo1', ''),
       (NULL, 'some description for todo2', ''),
       (NULL, 'some description for todo3', ''),
       ('todo 4', 'some description for todo4', ''),
       (NULL, 'some description for todo5', '');
SELECT LAST_INSERT_ID();