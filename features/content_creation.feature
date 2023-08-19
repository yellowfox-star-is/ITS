Feature: Creation, change and deletion of content.

    Background:
        Given An account with administrator privileges is logged in
        And Parent content exists

    Scenario: Creation of a new content
	Given User creates a new content
	When User fills all required inputs
	And User clicks 'Save'
	Then New content is created
	And Content is in the state 'Private'
	And Content is in a parent content (content viewed at the time of creation)

    Scenario: Change of a content
	Given Content edit is open
	When User changes input fields
	And User clicks 'Save' 
	Then Changed properties are changed
	And Changes are visible

    Scenario: User cuts a content
	Given Content was cut
	And Another content is viewed
	When User pastes
	Then Content's parent content is changed

    Scenario: User copies a content
	Given Content was copied
	And Another content is viewed
	When User pastes
	Then Copy of copied contend is created
	And New content's parent is viewed content
	And New content's state is 'Private'

    Scenario: User deletes a content
        Given Content exists
        And Content is being viewed
        And Deletion of the content is allowed
        When User deletes content
        Then Content is deleted
        And Content cannot be found anywhere
