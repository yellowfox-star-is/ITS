@fixture.publish_level.teardown
Feature: Change the content publishing level.
    
    Background:
        Given A content exists
        And User is viewing the content

    Scenario Outline: User sends back content
	Given "administrator" user is logged in
	And Content is in the "Published" state
	When User clicks 'State: "Published"'
	And User clicks 'Send back'
	Then Content's state is changed to 'Private'
	And "Consumers" can no longer see the content

    Scenario: Administrator publishes private content
	Given Administrator is logged in
	And Content is in the 'Private' state
	When Administrator clicks 'State: Private'
	And Administrator clicks 'Publish'
	Then Content's state is changed to 'Published'
	And Everyone can see the content

    Scenario Outline: Administrator submits private content for publication
	Given Administrator is logged in
	And Content is in the 'Private' state
	When Administrator clicks 'State: Private'
	And Administrator clicks 'Submit for publication'
	Then Content state is changed to 'Pending review'
	And Only "<viewers>" can see the content

    Examples: Viewing users
	| viewers |
	| administrators |
	| reviewers |

    Scenario Outline: User publishes pending review content
	Given Content is in the 'Pending review' state
	And "<type>" account is logged in
	When "<type>" clicks 'State: Pending review'
	And "<type>" clicks 'Publish'
	Then Content's state is changed to 'Published'
	And Everyone can see the content

    Examples: Users
	| type |
	| Administrator |
	| Reviewer |

    Scenario Outline: User sends back pending review content
        Given Content is in the 'Pending review' state
        And "<type>" account is logged in
        When "<type>" clicks 'State: Pending review'
        And "<type>" clicks 'Send back'
        Then Content's state is changed to 'Private'
        And Only Administrators can see the content

    Examples: Users
        | type |
        | Administrator |
        | Reviewer |


