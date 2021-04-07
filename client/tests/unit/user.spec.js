jest.mock("axios", () => ({
  get: jest.fn(() =>
    Promise.resolve({
      data: {
        id: 37,
        name: "asd",
        sectors: ["1", "3", "2"],
        success: true,
        terms: true,
      },
    })
  ),
  put: jest.fn(() =>
    Promise.resolve({
      data: {
        message: "resource updated",
      },
    })
  ),
}));
import { shallowMount } from "@vue/test-utils";
import User from "@/views/User.vue";
import axios from "axios";

let cmp;
beforeEach(() => {
  cmp = shallowMount(User);
  jest.resetModules();
  jest.clearAllMocks();
});

describe("User.vue", () => {
  it("renders the page", () => {
    expect(cmp.text()).toMatch(
      "Please enter your name and pick the Sectors you are currently involved in."
    );
  });

  it("calls get route on mount", async () => {
    await cmp.vm.getUser();

    expect(axios.get).toBeCalledWith("/users");
    expect(axios.get).toHaveBeenCalledTimes(1);
  });

  it("checks that put request is made on button click", async () => {
    const wrapper = shallowMount(User, {
      data() {
        return { sameUser: true, updatedName: 'asd', user: {name: 'asd'} };
      },
    });
    const saveButton = wrapper.findComponent({ ref: "saveButton" });

    saveButton.trigger("click");
    expect(axios.put).toBeCalledWith("/users", {
      id: null,
      sectors: null,
      terms: false,
    });
    expect(axios.get).toBeCalledWith("/users");

  });

  it("shows the error text if condition is true", () => {
    const wrapper = shallowMount(User, {
      data() {
        return { error: true };
      },
    });

    expect(wrapper.find(".error").exists()).toBe(true);
  });
});
