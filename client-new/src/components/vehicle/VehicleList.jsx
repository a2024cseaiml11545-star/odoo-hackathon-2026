import React from "react";

function VehicleList() {
  return (
    <div>
      <h2>Vehicle List</h2>

      <table border="1">
        <thead>
          <tr>
            <th>Vehicle No</th>
            <th>Name</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <tr>
  <td>UP32AB1234</td>
  <td>Bus 1</td>
  <td>Available</td>
  <td>
    <button>Edit</button>
    <button>Delete</button>
  </td>
</tr>

<tr>
  <td>UP32CD5678</td>
  <td>Bus 2</td>
  <td>On Trip</td>
  <td>
    <button>Edit</button>
    <button>Delete</button>
  </td>
</tr>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

export default VehicleList;