import React from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';

class Discussions extends React.Component {
  constructor(props) {
    super(props);
  }

  getComparisons() {
    const {content_authored} = this.props;
    const average_content = 7;

    return (
      <div className="chart-wrapper">
        You {content_authored}
        Others {average_content}
      </div>
    );
  }

  render() {
    const {content_authored, thread_votes} = this.props;

    return (
      <div className="discussions-wrapper">
        <h2 className="group-heading">Discussions</h2>
        <div className="comparison-charts">
          <h3 className="section-heading">Posts, comments, and replies</h3>
          {this.getComparisons()}
        </div>
        <div className="post-counts">
          <div className="votes-wrapper">
            <span className="fa fa-plus-square-o count-icon" aria-hidden="true"></span>
            <span className="user-count">{thread_votes}</span>
            <p className="label">Votes on your posts, comments, and replies</p>
          </div>
        </div>
      </div>
    );
  }
}


Discussions.propTypes = {
  content_authored: PropTypes.number.isRequired,
  thread_votes: PropTypes.number.isRequired
}

export default Discussions;
