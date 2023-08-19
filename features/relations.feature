Feature: Adding, customizing and removing relations.

    Background:
        Given Administrator account exists
        And Administrator account is logged in

    Scenario: Adding relation
        Given Content is being edited
        And Content was added in relations
        When User saves
        Then Relations are saved
        And Links to related content are shown in the Method

    Scenario: Removing relation
        Given Content is being edited
        And Relations to other content exists
        And Relation to other content is removed
        When User saves
        Then Relation to other content is removed
        And Links to related content is no longer shown in edited Content
