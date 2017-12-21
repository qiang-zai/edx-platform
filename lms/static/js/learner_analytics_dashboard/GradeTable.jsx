import React from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';
const exGrades = [  
  {  
    "assignment_type":"Exam",
    "total_possible":6.0,
    "total_earned":3.0
  },
  {  
    "assignment_type":"Homework",
    "total_possible":5.0,
  },
  {  
    "assignment_type":"Homework",
    "total_possible":11.0,
    "total_earned":0.0
  }
];

class GradeTable extends React.Component {
  constructor(props) {
    super(props);
  }
  
  getTableGroup(type, groupIndex) {
    const {data} = this.props;
    const groupData = data.filter(value => {
      if (value['assignment_type'] === type) {
        return value;
      }
    });
    const multipleAssessments = groupData.length > 1;

    const rows = groupData.map(({assignment_type, total_possible, total_earned, passing_grade}, index) => {
      const label = multipleAssessments ? `${assignment_type} ${index + 1}` : assignment_type; 
      return (
        <tr key={index}>
          <td>{label}</td>
          <td>{passing_grade}/{total_possible}</td>
          <td>{total_earned <= 0 ? '-' : total_earned}/{total_possible}</td>
       </tr>
      );
    });

    return <tbody className="type-group"
                  key={groupIndex}>{rows}</tbody>;
  }
  
  render() {
    const {assignmentTypes} = this.props;
    return (
      <table className="table grade-table">
        <thead className="table-head">
          <tr>
            <th>Assessment</th>
            <th>Passing</th>
            <th>You</th>
          </tr>
        </thead>
        {assignmentTypes.map((type, index) => this.getTableGroup(type, index))}
       </table>
    )
  }
};

GradeTable.propTypes = {
  data: PropTypes.array.isRequired
}

export default GradeTable;
