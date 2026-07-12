import React from "react";

function VehicleForm() {
  return (
    <div>
      <h2>Add Vehicle</h2>

      <input type="text" placeholder="Vehicle Number" />
      <br /><br />

      <input type="text" placeholder="Vehicle Name" />
      <br /><br />

      <select>
        <option>Available</option>
        <option>On Trip</option>
        <option>In Shop</option>
        <option>Retired</option>
      </select>
      <br /><br />

      <button>Add Vehicle</button>
    </div>
  );
}

export default VehicleForm;