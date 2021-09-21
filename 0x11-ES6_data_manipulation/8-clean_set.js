/* eslint-disable */
export default function cleanSet(set, startString) {
  const data = Array();
  if (startString !== "" && typeof startString === "string") {
    for (let element of set) {
      if (element instanceof String)
        if (element.startsWith(startString))
          data.push(element.slice(startString.length));
    }
    return data.join("-");
  }
  return "";
}
