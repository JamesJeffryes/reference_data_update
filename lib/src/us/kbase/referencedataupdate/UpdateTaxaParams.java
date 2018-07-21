
package us.kbase.referencedataupdate;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: UpdateTaxaParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "target_workspace",
    "selection_params",
    "bad_word"
})
public class UpdateTaxaParams {

    @JsonProperty("target_workspace")
    private String targetWorkspace;
    @JsonProperty("selection_params")
    private String selectionParams;
    @JsonProperty("bad_word")
    private String badWord;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("target_workspace")
    public String getTargetWorkspace() {
        return targetWorkspace;
    }

    @JsonProperty("target_workspace")
    public void setTargetWorkspace(String targetWorkspace) {
        this.targetWorkspace = targetWorkspace;
    }

    public UpdateTaxaParams withTargetWorkspace(String targetWorkspace) {
        this.targetWorkspace = targetWorkspace;
        return this;
    }

    @JsonProperty("selection_params")
    public String getSelectionParams() {
        return selectionParams;
    }

    @JsonProperty("selection_params")
    public void setSelectionParams(String selectionParams) {
        this.selectionParams = selectionParams;
    }

    public UpdateTaxaParams withSelectionParams(String selectionParams) {
        this.selectionParams = selectionParams;
        return this;
    }

    @JsonProperty("bad_word")
    public String getBadWord() {
        return badWord;
    }

    @JsonProperty("bad_word")
    public void setBadWord(String badWord) {
        this.badWord = badWord;
    }

    public UpdateTaxaParams withBadWord(String badWord) {
        this.badWord = badWord;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((("UpdateTaxaParams"+" [targetWorkspace=")+ targetWorkspace)+", selectionParams=")+ selectionParams)+", badWord=")+ badWord)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
