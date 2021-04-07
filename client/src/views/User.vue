<template>
  <div>
    <h2>
      Please enter your name and pick the Sectors you are currently involved in.
    </h2>
    <div :class="$style.error" v-if="error">There is an error, please try again!</div>
    <div :class="$style.error" v-if="invalidUser">Please fill all the fields to create a user</div>
    <div :class="$style.row">
      <label>Name</label>
      <EditComp :value="user.name" @input="updateName" />
    </div>
    <div :class="$style.row">
      <label>Sectors</label>
      <Treeselect :sectors="user.sectors" @updatedSectors="updateSectors" />
    </div>
    <div :class="$style.row">
      <label>Agree to terms</label>
      <input
        v-model="user.terms"
        :value="user.terms"
        :class="$style.checkbox"
        type="checkbox"
      />
    </div>
    <button ref="saveButton" @click="save" :class="$style.button">Save</button>
  </div>
</template>

<script>
import EditComp from "../components/input-edit";
import axios from "axios";
import Treeselect from "../components/tree-select";

export default {
  data: () => ({
    error: false,
    invalidUser: false,
    updatedName: "",
    updatedSectors: null,
    user: {
      sectors: null,
      name: "",
      terms: false,
      id: null,
    },
    sameUser: true,
  }),

  mounted() {
    this.getUser();
  },

  watch: {
    updatedName(newVal, oldVal) {
      if (newVal !== oldVal) {
        this.sameUser = false;
      }
    },
  },

  methods: {
    updateName(value) {
      this.updatedName = value;
    },
    
    updateSectors(value) {
      this.updatedSectors = value;
    },

    async save() {
      if (this.sameUser === true || this.updatedName === this.user.name) {
        try {
          this.error = false;
           if (this.updatedName.length === 0) return (this.error = true);
          await axios.put("/users", {
            id: this.user.id,
            sectors: this.updatedSectors,
            terms: this.user.terms,
          });

          await this.getUser();
        } catch (ex) {
          this.error = true;
        }
      } else {
        try {
          this.error = false;
          if (this.updatedName.length === 0) return (this.error = true);

          await axios.post("/users", {
            sectors: this.updatedSectors,
            name:
              this.updatedName.length === 0 ? this.user.name : this.updatedName,
            terms: this.user.terms,
          });

          await this.getUser();
        } catch (ex) {
          this.error = true;
        }
      }
    },

    async getUser() {
      try {
        this.invalidUser = false;
        const { data } = await axios.get("/users");
        this.user = data;
      } catch (ex) {
        this.invalidUser = true;
      }
    },
  },

  components: { Treeselect, EditComp },
};
</script>

<style module lang="scss">
.row {
  display: flex;
  align-items: center;
  max-width: 40rem;
  margin-bottom: 2rem;
  justify-content: flex-start;
  > label {
    min-width: 10rem;
  }
}

.input {
  padding-left: 0.3125rem;
  padding-right: 0.3125rem;
  width: 100%;
  height: 36px;
  border: 1px solid #ddd;
  border-radius: 0.3125rem;
  outline: none;
  color: #2c3e50;
}

.checkbox {
  width: 1.5rem;
  height: 1.5rem;
  margin: 0;
}

.button {
  outline: none;
  background: rgb(66, 132, 255);
  color: #fff;
  border: none;
  padding: 0.5rem;
  border-radius: 0.3125rem;
  cursor: pointer;

  &:hover {
    background: rgb(96, 151, 251);
  }
}

.error {
  color: red;
  margin-bottom: 1rem;
}
</style>
