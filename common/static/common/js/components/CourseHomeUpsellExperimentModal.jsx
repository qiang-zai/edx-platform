import React from 'react';

import { UpsellExperimentModal } from './UpsellExperimentModal.jsx';

// https://openedx.atlassian.net/browse/LEARNER-3583

export class CourseHomeUpsellExperimentModal extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        // This content will be updated in the future
        return (
            <UpsellExperimentModal
                slides={[
                    (<div>
                        <span>My Stats introduces new personalized views that help you track your progress towards completing your course!</span>
                        <p />
                        <span>With My Stats you will see your:</span>
                        <ul>
                            <li><b>Course Activity Streak</b> (log in every week to keep your streak alive)</li>
                            <li><b>Grade Progress</b> (see how you're tracking towards a passing grade)</li>
                            <li><b>Discussion Forum Engagements</b> (top learners use the forums - how do you measure up?)</li>
                        </ul>
                    </div>),
                    (<div>
                        <div><b>Course Activity Streak</b></div>
                        <p />
                        <span>Log into the course every week to keep your activity streak alive. See how many of your fellow learners have logged in this past week.</span>
                    </div>),
                    (<div>
                        <div><b>Grade Progress</b></div>
                        <p />
                        <span>Keep track of your current grade and compare it with passing grade to see where you need to study in order to stay on track.</span>
                    </div>),
                    (<div>
                        <div><b>Discussion engagements</b></div>
                        <p />
                        <span>Compare your forum posts with others who have previously graduated this course.</span>
                    </div>),
                ]}
                modalTitle="My Stats"
                buttonLabel="Upgrade ($100 USD)"
                buttonDisplay="Upgrade ($100 USD)"
                buttonDestinationURL='https://edx.org'
            />
        )
    }
}

